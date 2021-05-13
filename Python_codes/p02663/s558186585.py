a,b,c,d,k = map(int,input().split())
t = c*60+d - (a*60+b)
print(max(0,t-k))