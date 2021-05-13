N=int(input())
print((N+1) * (N // 2) - N if N%2==0 else (N+1) * (N // 2) + int(N/2+1) - N)