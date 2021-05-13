def digit(x):
    cnt = 0
    if x == 0: cnt = 1
    else:
        while x > 0:
            x //= 10
            cnt+=1
    return cnt
n = int(input())
ans = 0
for i in range(1,n+1):
    if digit(i) % 2 == 1: 
        ans+=1
print(ans)