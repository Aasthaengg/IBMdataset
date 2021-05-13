h, w = map(int, input().split())
s = ""
cnt = [0] * 26
for _ in range(h):
    s = input()
    for i in range(len(s)):
        cnt[ord(s[i]) - ord("a")] += 1
#print(cnt)
c4=0
c2=0
c1=0
if h&1 == 1:
    c2 += w // 2
if w&1 == 1:
    c2 += h // 2
if (h&1 == 1) and (w&1 == 1):
    c1 = 1
c4 += (h//2) * (w//2)
#print(c1,c2,c4)

for i in range(26):
    if c4 <= 0:
        continue
    while cnt[i] >= 4:
        cnt[i] -= 4
        c4 -= 1
for i in range(26):
    if c2 <= 0:
        continue
    while cnt[i] >= 2:
        cnt[i] -= 2
        c2 -= 1
for i in range(26):
    if c1 <= 0:
        continue
    while cnt[i] % 4 == 1 or cnt[i] % 4 == 3:
        cnt[i] -= 1
        c1 -= 1

#print(c1,c2,c4)
if c1==0 and c2==0 and c4==0:
    print("Yes")
else:
    print("No")