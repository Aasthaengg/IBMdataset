N=int(input())
A=list(map(int,input().split()))

check=1
ans=0

ans_flag=False

for a in A:
    if a==check:
        ans_flag=True
        check += 1
        
    else:
        ans += 1
        
if ans_flag == False:
    ans=-1
    
print(ans)