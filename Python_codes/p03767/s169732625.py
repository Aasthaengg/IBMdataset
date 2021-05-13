n = int(input())

s = list(map(int,input().split()))

s.sort(reverse = True)

ans = 0

for i in range(1,2*n+1,2):
    ans += s[i]
    
print(ans)