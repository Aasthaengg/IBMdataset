N,A,B = map(int,input().split())
h = [int(input()) for i in range(N)]

l = 0
r = 10**9

while r-l>1:
    tmp = (l+r)//2

    count = 0#Aの処理(A-B)を余ったところに適用していく
    for i in range(N):
        count += max(0,h[i]-B*tmp)//(A-B)
        if max(0,h[i]-B*tmp)%(A-B) != 0:
            count+=1
    
    if tmp >= count:
        r = tmp
    else:
        l=tmp

print(r)