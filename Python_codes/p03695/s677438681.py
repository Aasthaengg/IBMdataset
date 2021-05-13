N = int(input())
a = list(map(int,input().split()))
C = [0]*9
for e in a:
    if e < 400:
        C[0] += 1
    elif e < 800:
        C[1] += 1
    elif e < 1200:
        C[2] += 1
    elif e < 1600:
        C[3] += 1
    elif e < 2000:
        C[4] += 1
    elif e < 2400:
        C[5] += 1
    elif e < 2800:
        C[6] += 1
    elif e < 3200:
        C[7] += 1
    else:
        C[8] += 1
ans = 0
for k in range(8):
    if C[k] > 0:
        ans += 1
print(max(1,ans),ans+C[8])
