n=int(input())
H=list(map(int,input().split()))
cnt=0
cnts=[]
for i in range(len(H)-1):
    if H[i]>=H[i+1]:
        cnt+=1
    else:
        cnts.append(cnt)
        cnt=0
cnts.append(cnt)
#print(cnts)
print(max(cnts))
