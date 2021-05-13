[H,W] = list(map(int,input().split()))
N = int(input())
a = list(map(int,input().split()))

flag=0  #left-->right

out = [[0]*W for i in range(H)]
# print(*out, sep="\n")

dammy=0
k=0
l=0
for i in range(N):
    # print('a:',a[i])
    for j in range(a[i]):
        out[k][l] = i+1
        if l==W-1:
            l=0
            k+=1
        else:
            l+=1
    # print('out:',out)


#reverse
for i in range(H):
    if i%2==1:
        #out[i] = reversed(out[i])
        out[i].reverse()
        print(*out[i])
    else:
        print(*out[i])
