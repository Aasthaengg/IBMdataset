N = int(input())
P = list(map(int, input().split()))

sort_P = list(range(1, N+1))
wrong = 0

for i in range(N):
    if P[i] != sort_P[i]:
        wrong += 1

if wrong > 2:
    print("NO")
else:
    print("YES")