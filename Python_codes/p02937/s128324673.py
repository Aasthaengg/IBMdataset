import bisect

s = input()
t = input()

li = [[] for _ in range(26)]
for i in range(len(s)):
    li[ord(s[i]) - ord('a')].append(i)

count = [0,-1]

for i in range(len(t)):
    t1 = t[i]
    num = ord(t1) - ord('a')
    if not li[num]:
        print(-1)
        exit()
    else:
        if count[1] >= li[num][-1]:
            count[0] += 1
            count[1] = li[num][0]
        else:
            idx = bisect.bisect_right(li[num], count[1])
            count[1] = li[num][idx]

print(count[0] * len(s) + count[1] + 1)
