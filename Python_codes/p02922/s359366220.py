a,b=map(int,input().split())
k=1
for i in range(21):
    if k<b:
        k+=a-1
    else:
        print(i)
        break