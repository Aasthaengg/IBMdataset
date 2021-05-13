n=int(input());a=list(map(int,input().split()))
print('NYOE S'[sum([i==j for i,j in zip(a,sorted(a))])>=n-2::2])