N = int(input())
result=0
for i in range(1,N+1,2):
    j= i+1
    cnt=0

    for k in range(1,j):
        if i % k==0:

            cnt+=1

            if cnt>8:
                break
    
    if cnt == 8:
        result+=1
    
print(result)
