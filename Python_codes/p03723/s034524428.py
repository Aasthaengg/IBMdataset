*a,=map(int,input().split())
b=[bin(abs(a[i+1]-a[i]))[::-1].find('1') for i in range(2)]
print((max(b) if b[0]*b[1]<0 else min(b))*(1-sum(a)%2))