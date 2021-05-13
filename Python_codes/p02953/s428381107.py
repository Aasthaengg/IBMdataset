
N = int(input())
X = list(map(int, input().split()))

cur = 0
flag = True
for i in range(N):
    cur = max(cur, X[i])
    if cur - X[i] > 1:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
