a,b,c = map(int,input().split())

ans = int( a*b*c/(max(a,b,c)*2) )

print(ans)