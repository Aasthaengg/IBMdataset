import itertools

n = int(input())
s = [input() for i in range(n)]

cnt = [0]*5
for i in range(n):
    if s[i][0]== 'M':
      cnt[0] += 1
    elif s[i][0]== 'A':
      cnt[1] += 1
    elif s[i][0]== 'R':
      cnt[2] += 1
    elif s[i][0]== 'C':
      cnt[3] += 1
    elif s[i][0]== 'H':
      cnt[4] += 1
cnt.sort()
# print(cnt)
p = 0
if cnt[2] == 0:
    p = 0
elif cnt[1] == 0:
    p = cnt[2]*cnt[3]*cnt[4]
elif cnt[0] == 0:
    p += cnt[1]*cnt[2]*cnt[3]
    p += cnt[1]*cnt[2]*cnt[4]
    p += cnt[1]*cnt[3]*cnt[4]
    p += cnt[2]*cnt[3]*cnt[4]
else:
    num = [0,1,2,3,4]
    combi = list(itertools.combinations(num,3))
    # print(combi)
    for i in range(len(combi)):
        a,b,c = combi[i][0], combi[i][1], combi[i][2]
        p += cnt[a]*cnt[b]*cnt[c]
print(p)