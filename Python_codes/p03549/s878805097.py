N,M=map(int,input().split())
ans = 0
r = (1/2)**M
time = 1900*M + 100*(N-M)
ans = time *(1/r)
print(int(ans))