n = int(input())
atob = []
ans = 0
for i in range(n):
    x,y = map(int,input().split())
    ans += x
    atob.append(x+y)
    
atob.sort(reverse=True)

for i in range(n//2):
    ans -= atob[2*i+1]
    
print(ans)