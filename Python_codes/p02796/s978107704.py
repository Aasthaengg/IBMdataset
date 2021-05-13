n = int(input())
s = [[]]*n
for i in range(n):
    x, l = map(int,input().split())
    s[i] = [x-l, x+l]
s.sort(key = lambda x : x[1])

n = len(s)
cnt = 1

for i in range(1,n):
    if s[i-1][1] > s[i][0]:
        s[i][1] = s[i-1][1]
    else:
        cnt += 1

print(cnt)