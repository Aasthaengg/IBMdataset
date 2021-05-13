N = int(input())
D, X = map(int, input().split())
ans = 0
for i in range(N):
    num = float(D)/int(input())
    if num.is_integer(): ans += int(num)
    else: ans += int(num)+1
print(ans+X)

    
    

