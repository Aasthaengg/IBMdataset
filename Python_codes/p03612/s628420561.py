N = int(input())
P = tuple(map(int, input().split(' ')))

i = 0
ans = 0
while i < N:
    if P[i] == i + 1:
        if i < N - 1 and P[i + 1] == i + 2:
            ans += 1
            i += 1
        else:
            ans += 1
    i += 1

print(ans)
