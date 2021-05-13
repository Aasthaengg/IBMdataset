N, K =map(int, input().split())
mod = 10**9 + 7
A = int(-(N+1)*(N+2)*(2*N+3)/6)%mod
B = int((N+1)*(N+1)*(N+2)/2)%mod
C = N+1
a = int(-(K-1)*K*(2*K-1)/6)%mod
b = int((N+1)*(K-1)*K/2)%mod
c = K-1
print((A+B+C-a-b-c)%mod)