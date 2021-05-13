N = int(input())
X = list(map(int, input().split()))
sx = sorted(X)
lm = sx[N//2-1]
rm = sx[N // 2]
for i in range(N):
    if X[i] <= lm:
        print(rm)
    else:
        print(lm)
