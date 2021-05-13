n = int(input())
a = list(map(int,input().split()))

ans = 0
up = 0
down = 0
i=0

while (i+1)<n:
    if up == down:
        if a[i+1] > a[i]:
            up += 1
            down = 0
        elif a[i+1] < a[i]:
            up = 0
            down += 1
        else:
            up += 1
            down += 1
    elif up == 0 and down !=0:
        if a[i+1] <= a[i]:
            down += 1
        else:
            ans += 1
            down = 0
    elif down == 0 and up!= 0:
        if a[i+1] >= a[i]:
            up += 1
        else:
            ans += 1
            up = 0
    i += 1

print(ans+1)