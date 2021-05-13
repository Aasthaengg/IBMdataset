n,a,b = map(int,input().split(' '))
minvalue = a*(n-1)+b
maxvalue = b*(n-1)+a
ans = (maxvalue-minvalue+1)
print(max(ans,0))