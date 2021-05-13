
n,m = map(int,input().split())

x = list(map(int,input().split()))
y = list(map(int,input().split()))

xsum = 0

up = 1
down = n-1

for i in range(n-1):

    xsum += (x[i+1] - x[i]) * up * down
    xsum %= (10 ** 9 + 7)

    up += 1
    down -= 1

left = 1
right = m-1

ans = 0

for i in range(m-1):

    ans += (y[i+1] - y[i]) * left * right * xsum
    ans %= (10 ** 9 + 7)

    left += 1
    right -= 1

print (ans)
        
