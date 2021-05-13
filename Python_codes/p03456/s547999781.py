a,b = map(int,input().split())

num = int(str(a)+str(b))
ans = 'No'

for i in range(1,401):
    if num == i**2:
        ans = 'Yes'
        break
        
print(ans)