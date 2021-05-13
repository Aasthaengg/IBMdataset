a,b,c=map(int,input().split())
ab = a+b
ac = a+c
bc = b+c

ans = min(ab,ac,bc)
print(ans)
