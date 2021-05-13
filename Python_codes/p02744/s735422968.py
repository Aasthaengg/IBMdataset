from collections import deque
n = int(input())
abc = 'abcdefghij'
s = ''
cnt = 0
ans = deque([s])
while True:
    a = ans.popleft()
    cnt = len(a)
    if cnt == n:
        ans.append(a)
        break
    kind = len(set(a)) + 1
    for i in range(kind):
        ans.append(a + abc[i])

for i in sorted(ans):
    print(i)

