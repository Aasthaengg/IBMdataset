"""
全探索
"""
n = int(input())
ans = 0
for num in range(1,n+1) :
    if len(str(num))%2 :
        ans += 1
print(ans)
