n = int(input())
ans = 0
a = 0
b = 0
ryou = 0
for _ in range(n):
    tmp = input()
    ans += tmp.count('AB')
    if tmp[0] == 'B':
        if tmp[-1] == 'A':
            ryou += 1
        else:
            b += 1
    elif tmp[-1] == 'A':
        a += 1

if ryou > 1:
    ans += (ryou-1)
    ryou = 1
if ryou == 1:
    if a >= 1:
        ans += 1
        a -= 1
    if b>=1:
        ans += 1
        b-=1
#print(ans)
ans += min(a,b)
#print(min(a,b))
print(ans)