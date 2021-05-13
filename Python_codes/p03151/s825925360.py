n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a)<sum(b):
    print(-1)
    exit()
dif_posi=[]
dif_nega=0
cnt=0
for x,y in zip(a,b):
    if x-y<0:
        dif_nega+=x-y
        cnt+=1
    else:
        dif_posi.append(x-y)

dif_posi=sorted(dif_posi,reverse=True)
for i in dif_posi:
    if dif_nega >= 0:
        break
    dif_nega+=i
    cnt+=1

print(cnt)