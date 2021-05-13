N = int(input())
X = list(map(int, input().split()))
sort_X = sorted(X)
a = sort_X[N//2-1]
b = sort_X[N//2]
for i in range(N):
    if X[i] < b:
        print(b)
    else:
        print(a)