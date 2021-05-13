n = int(input())
f = [list(map(int,input().split())) for i in range(n)]
p = [list(map(int,input().split())) for i in range(n)]
print(max(sum(p[j][sum(i>>k&1 and f[j][k] for k in range(10))] for j in range(n)) for i in range(1,2**10)))
