N,H,W = map(int,input().split())
size=[]
cnt=0
for i in range(N):
    array=list(map(int,input().split()))
    if array[0]>=H and array[1]>=W :
        cnt=cnt+1
print(cnt)