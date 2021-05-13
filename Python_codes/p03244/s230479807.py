from collections import Counter

n = int(input())
l = list(map(int, input().split()))

d1 = Counter(l[::2]).most_common()
d2 = Counter(l[1::2]).most_common()
d1.append([0,0])
d2.append([0,0])

if d1[0][0] != d2[0][0]:
    print(n//2-d1[0][1] + n//2-d2[0][1])
else:
    ans1 = n//2 - d1[0][1] + n//2 - d2[1][1]
    ans2 = n//2 - d1[1][1] + n//2 - d2[0][1]
    print(min(ans1, ans2))

