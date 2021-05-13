a,b = list(map(int,input().split()))
l = sum(list(map(int,input().split())))
print(a-l if a-l > -1 else -1)