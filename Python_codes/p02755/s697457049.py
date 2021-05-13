import sys
#h,w=map(int,input().split())
#S=[list(map(int,input().split())) for _ in range(h)]
a,b=map(int,input().split())
for i in range(2000):
    if int(i*8/100)==a and int(i*10/100)==b:
        print(i)
        exit()
print(-1)
