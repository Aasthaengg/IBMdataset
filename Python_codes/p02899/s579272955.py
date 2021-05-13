N = int(input())
A = list(map(int, input().split()))
d = {a:i for i,a in enumerate(A,1)}
ans = [d[i] for i in range(1,N+1)]
print(*ans)