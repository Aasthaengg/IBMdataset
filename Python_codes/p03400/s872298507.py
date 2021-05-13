n = int(input())

d,x = map(int,input().split())

a = []

for i in range(n):
    a.append(int(input()))
    
ans = 0

for i in a:
    for _ in range(1,d+1,i):
        ans += 1
        
print(ans+x)

