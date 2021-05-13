N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
happy_kid = 0
for i in range(N):
    x = x - a[i]
    if i == N - 1:
        if 0 == x:
            happy_kid += 1
    elif x >= 0:
        happy_kid += 1
    else:
        break
print(happy_kid)