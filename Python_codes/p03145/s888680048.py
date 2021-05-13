a,b,c = map(int,input().split())
print(min(a,b,c)*(sum([a,b,c])-min(a,b,c)-max(a,b,c))//2)
