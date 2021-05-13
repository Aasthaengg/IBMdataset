a, b = map(int, input().split())
cnt=1
while True:
    a=a*2
    if(a>b):
        print(cnt)
        break
    cnt+=1