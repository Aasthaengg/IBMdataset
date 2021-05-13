import math
abc = [int(input()) for _ in range(5)]
tmp = 9
ans = 0
ii = 0
for i in range(5):
    tmpp = min(tmp, (abc[i]-1)%10)
    if tmp != tmpp:
        tmp = tmpp
        ii = i
for i in range(5):
    if i == ii:
        ans += abc[i]
    else:
        ans += (math.ceil(abc[i]/10))*10
print(ans)