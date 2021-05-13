n=int(input())
b=list(map(int,input().split()))
ba=[]#右からの距離を足したやつ
for i in range(n):
    if len(ba)<b[i]-1:
        print(-1)
        break
    else:
        ba.insert(b[i]-1,b[i])
else:
    for i in range(n):
        print(ba[i])