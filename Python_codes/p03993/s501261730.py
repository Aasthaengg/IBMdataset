N=int(input())
like=list(map(int,input().split()))
count=0

for i in range(N):
    like_1=like[i]
    #print("like_1")
    #print(like_1)
    if like[like_1-1]==i+1:
        #print(like[like_1-1])
        #print(i+1)
        count+=1
        #print("///")
        
print(count//2)