a,b=map(int,input().split())
h=list(map(int,input().split()))
h.sort()
print(sum(h[-b:]))