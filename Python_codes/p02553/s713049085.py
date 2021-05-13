a,b,c,d = list(map(int,input().split()))
best = max(a*c, a*d, b*c, b*d)
print(best)