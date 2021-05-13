N = int(input())
A = list(map(int, input().split()))

temp = 1
ans = 1
for a in A:
    if a % 2 == 0:
        temp *= 2
        ans *= 3
    else:
        temp *= 1
        ans *= 3

print(ans - temp)