N=int(input())
S=input()
ans=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            count=0
            for s in S:
                if count==0:
                    if s==str(i):
                        count+=1
                elif count==1:
                    if s==str(j):
                        count+=1
                elif count==2:
                    if s==str(k):
                        count+=1
                if count==3:
                    ans+=1
                    break
print(ans)