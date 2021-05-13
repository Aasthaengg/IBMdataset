*a,=map(int,input().split())
b=[bin(a[i+1]-a[i])[::-1].find('1')for i in (0,1)]
print((max(b)*(b[0]*b[1]<0) or min(b))*(1-sum(a)%2))