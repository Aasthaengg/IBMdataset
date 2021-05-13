N = int(input())
S_list = [input() for x in range(N)]
#print(S_list)

# Aで終わる、かつ、Bで始まらない
a_count = 0
# Aで終わらない、かつ、Bで始まる
b_count = 0
# Aで終わる、かつ、Bで始まる
ab_count = 0

for s in S_list:
    if s[0] != "B" and s[-1] == "A":
        a_count += 1
    elif s[0] == "B" and s[-1] != "A":
        b_count += 1
    elif s[0] == "B" and s[-1] == "A":
        ab_count += 1

# 単体で含まれる"AB"の数
temp = sum([x.count("AB") for x in S_list])

if ab_count == 0:
    print(temp + min(a_count, b_count))
else:
    # a_count、b_countともに0の場合
    if a_count == 0 and b_count == 0:
        print(temp + ab_count - 1)

    # a_count または b_count が0でない場合
    else:
        print(temp + min(a_count, b_count) + ab_count)
