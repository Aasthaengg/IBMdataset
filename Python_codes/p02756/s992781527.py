s=input()
q=int(input())

rev=0

left=""
right=""

for i in range(q):
    
    x = list(map(str,input().split()))
    
    if int(x[0]) == 1:
        rev ^= 1
        
    else:
        if int(x[1])-1 ^ rev == 0:
            left = x[2] + left
        else:
            right = right + x[2]
            
ans = left + s + right

if rev==1:
    ans=ans[::-1]
        
print(ans)
