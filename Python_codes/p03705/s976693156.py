n,a,b = map(int,input().split())
minA = a*(n-1)+b
maxA = b*(n-1)+a
print(max(maxA-minA+1,0))