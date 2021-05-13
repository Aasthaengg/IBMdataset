inp=sorted(list(map(int,input().split())))
while inp[1]>=inp[0]:
    a=inp[1]%inp[0]
    if a==0:
        break
    inp[1]=inp[0]
    inp[0]=a

print(inp[0])
