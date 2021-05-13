N = int(input())
P = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if P[i] == i+1:
        pass
    else:
        cnt += 1

if (cnt == 0) or (cnt == 2):
    print("YES")
else:
    print("NO")
