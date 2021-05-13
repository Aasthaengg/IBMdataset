n = int(input())
l = list(map(int,input().split()))
ans = 0
now = 0
m = 0
c = 0
for i in l:
    if now == 0:
        now = i
    else:
        if m == 0:
            if now < i:
                m = 1
            elif now > i:
                m = -1
        elif m == 1:
            if now > i:
                ans += 1
                m = 0
            
        else:
            if now < i:
                ans += 1
                m = 0
        now = i

print(ans+1)