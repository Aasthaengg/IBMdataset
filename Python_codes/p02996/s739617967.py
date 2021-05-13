n = int(input())
ba = []
now = 0
ans = "Yes"

for _ in range(n):
    a,b = map(int,input().split())
    ba.append([b,a])
    
ba = sorted(ba)

for i in range(n):
    now += ba[i][1]
    
    if ba[i][0] < now:
        ans = "No"
        break
        
print(ans)