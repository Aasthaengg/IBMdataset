N,M=map(int,input().split())

OK,NG=N-M,M
exp=2**NG
print(exp*(100*OK+1900*NG))
