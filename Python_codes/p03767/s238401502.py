N = int(input())
A = sorted(list(map(int,input().split())),key=lambda x: -x)[:2*N]
ans = 0
for i in range(1,2*N,2):
    ans += A[i]
print(ans)