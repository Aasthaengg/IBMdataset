s = input()
cnt = [0]*3
for i in s:
    cnt[ord(i)-ord('a')] += 1
if max(cnt)-min(cnt)<=1:
    print('YES')
else:
    print('NO')