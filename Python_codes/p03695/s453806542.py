N = int(input())
A = list(map(int,input().split()))
b = [0]*9
for a in A:
    if a <400:
        b[0] += 1
    elif a < 800:
        b[1] += 1
    elif a < 1200:
        b[2] += 1
    elif a < 1600:
        b[3] += 1
    elif a < 2000:
        b[4] += 1
    elif a < 2400:
        b[5] += 1
    elif a < 2800:
        b[6] += 1
    elif a < 3200:
        b[7] += 1
    else:
        b[8] += 1
ans = 8
for B in b[:8]:
    if B == 0:
        ans -= 1
ans2 = ans+b[8]
if ans == 0:
    ans = 1
print(ans,ans2)