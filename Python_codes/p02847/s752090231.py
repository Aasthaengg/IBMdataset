# 146a

#日曜からの日数を指定
SUN_N = 0
MON_N = 1
TUE_N = 2
WED_N = 3
THU_N = 4
FRI_N = 5
SAT_N = 6

S = input() # 曜日を入力

if S == 'SUN':
    From_days = SUN_N
elif S == 'MON':
    From_days = MON_N
elif S == 'TUE':
    From_days = TUE_N
elif S == 'WED':
    From_days = WED_N
elif S == 'THU':
    From_days = THU_N
elif S == 'FRI':
    From_days = FRI_N
elif S == 'SAT':
    From_days = SAT_N
else:
    From_days = -99

To_days = 7 - From_days

print(To_days)
