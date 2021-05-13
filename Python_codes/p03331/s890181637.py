def digitsum(N):
    return sum(map(int,list(str(N))))
N = int(input())
m = 100000
for A in range(1,N//2+1):
    B = N-A
    m = min(m,digitsum(A)+digitsum(B))
print(m)