a,b,c = sorted(map(int,input().split()))
c1,c2 = c//2,-(-c//2)
print(a*b*(c2-c1))