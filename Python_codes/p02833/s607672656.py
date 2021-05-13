n=int(input())
cnt=0
if n%2==0:
    for i in range(1,30):
        cnt+=n//((5**i)*2)
    print(cnt)
else:
    print(0)
