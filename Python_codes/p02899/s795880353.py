N = int(input())
A = list(map(int, input().split()))
ans = {a:i for i,a in enumerate(A,1)}

for i in range(N):
    print(ans[i+1])