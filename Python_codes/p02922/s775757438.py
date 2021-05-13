a,b = list(map(int,input().split()))
count = 1
ans = 0

while count < b:
    count += (a-1)
    ans += 1
    
print(ans)