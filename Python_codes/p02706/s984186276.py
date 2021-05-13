n, m = map(int,input().split())
a = list(map(int,input().split()))

aa = sum(a) 
if n<aa:
    print(-1) 
else:
    print(n-aa)

