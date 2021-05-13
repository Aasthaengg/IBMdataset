# 今日の曜日を表す文字列 Sが与えられます。
# Sは SUN,MON,TUE,WED,THU,FRI,SAT のいずれかであり、
# それぞれ日曜日、月曜日、火曜日、水曜日、木曜日、金曜日、土曜日を表します。
# 次の日曜日 (あす以降) が何日後か求めてください。

# 標準入力から曜日（S）を取得する
input_weekday = input()

# 次の日曜日はあと何日後かを計算して出力する
result = 0
if input_weekday == 'SUN':
    result = 7
elif input_weekday == 'MON':
    result = 6
elif input_weekday == 'TUE':
    result = 5
elif input_weekday == 'WED':
    result = 4
elif input_weekday == 'THU':
    result = 3
elif input_weekday == 'FRI':
    result = 2
elif input_weekday == 'SAT':
    result = 1

print(result)
