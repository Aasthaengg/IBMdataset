from itertools import groupby
s = input()
k = int(input())
ans = 0
count = []
for i, j in groupby(s):
    count.append(len(list(j)))
if len(set(s)) == 1:
    ans = (len(s)*k)//2
elif k > 1 and s[0] == s[-1]:
    f = count[0]
    e = count[-1]
    ans += f//2 + e//2 + (f+e)//2*(k-1)
    for n in count[1:-1]:
        ans += n//2 * k
else:
    for n in count:
        ans += n//2 * k
print(ans)
