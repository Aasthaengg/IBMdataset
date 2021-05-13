s = input()
counter = [0]*2019
counter[0] = 1
ans = 0
res, d = 0, 1
for i in range(len(s)-1, -1, -1):
    res = (res+int(s[i])*d)%2019
    counter[res] += 1
    d = d*10%2019
for count in counter:
    ans += count*(count-1)//2
print(ans)