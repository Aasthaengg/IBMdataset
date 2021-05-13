N = int(input())
K = int(input())
X = [x for x in map(int,input().split())]

ans = 0

for x in X:
    if abs(x)<=abs(x-K):
        ans += 2*x
    else:
        ans += 2*abs(x-K)
print(ans)