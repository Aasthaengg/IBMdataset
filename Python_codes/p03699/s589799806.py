n = int(input())
s = [int(input()) for _ in range(n)]
sum = 0
for i in range(n):
    sum += s[i]
if sum % 10 != 0:
    print(sum)
else:
    s = sorted(s)
    for j in range(n):
        if s[j] % 10 != 0:
            sum = sum - s[j]
            print(sum)
            break
    if sum % 10 == 0:
        print(0)
