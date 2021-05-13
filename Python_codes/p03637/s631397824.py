n = int(input())
A = list(map(int,input().split()))
ans = "No"

odd = 0
even = 0
four = 0

for i in A:
    if i % 4 == 0:
        four += 1
    elif i % 2 == 0:
        even += 1
    else:
        odd += 1
        
if four >= even + odd - 1:
    ans = "Yes"

if four >= odd and even > 1:
    ans = "Yes"
    
print(ans)