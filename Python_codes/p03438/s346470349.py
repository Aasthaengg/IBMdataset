N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum_diffA = 0
sum_diffB = 0
for i, (ai, bi) in enumerate(zip(A,B)):
    if ai == bi:
        continue
    elif ai > bi:
        sum_diffB += (ai - bi)
    elif ai < bi:
        diffA = (bi - ai)
        sum_diffA += diffA // 2 + diffA % 2
        sum_diffB += diffA % 2
if sum_diffA >= sum_diffB:
    print('Yes')
else:
    print('No')
