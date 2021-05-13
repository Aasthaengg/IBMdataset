h,w = map(int,input().split())
c=[input() for _ in range(h)]
for i in range(1,h*2+1):
    print(c[(i+1)//2-1])