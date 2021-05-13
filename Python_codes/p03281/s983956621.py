"""
全探索
"""
n = int(input())
ans = 0
for num in range(1,n+1) :
    count = 0
    for i in range(1,num+1) :
        if num%i == 0 :
            count += 1
    if count == 8 and num%2 :
        ans += 1
print(ans)
