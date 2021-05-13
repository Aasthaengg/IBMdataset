h,a=map(int,input().split())
for i in range(10**100):
    if h <= a*i:
        print(i)
        break