n = int(input())
s = [int(input()) for s in range(n)]
s1 = []
sum0 = 0
for i in s:
    if i%10 == 0:
        sum0 += i
    else:
        s1.append(i)

if len(s1) == 0:
    print(0)
else:
    sum1 = sum(s1)
    if sum1%10 != 0:
        print(sum0 + sum1)
    else:
        print(sum0 + sum1 - min(s1))