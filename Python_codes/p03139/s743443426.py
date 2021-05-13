n,a,b = map(float,input().split())
print(int(min(a,b)), int(max(a+b-n, 0)))