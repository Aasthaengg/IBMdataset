K = int(input())
N = 50
r = (K-1)%N+1
q = (K-r)//N
a = [N+q]*r + [N+q-r-1]*(N-r)
print(N)
print(*a)