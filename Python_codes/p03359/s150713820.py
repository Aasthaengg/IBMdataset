a,b = map(int,input().split())
print(a-1+max(min(b//a,1),0))