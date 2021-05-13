n = int(input())
S = input()

ans = 0
for i in range(1000):
    nows = S
    istr = str(i).zfill(3)
    idx = nows.find(istr[0])
    if idx == -1:  continue
    nows = nows[idx+1:]
    idx = nows.find(istr[1])
    if idx == -1:  continue
    nows = nows[idx+1:]
    idx = nows.find(istr[2])
    if idx == -1:  continue
    ans += 1
print(ans)
