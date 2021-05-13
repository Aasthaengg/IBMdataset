h,a = map(int, input().split()) 

cnt=0
while True:
    h-=a
    cnt+=1
    if h<=0:
        print(cnt)
        exit()