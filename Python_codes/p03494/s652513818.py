n = int(input())
a = list(map(int,input().split()))

def cnt(n):
    x = 0
    while n%2 == 0:
        x += 1
        n = n//2
    return x
    
ans = 10**9

for i in a:
    ans = min(ans,cnt(i))
    
print(ans)