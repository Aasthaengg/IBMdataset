from collections import deque
n,c,k = map(int,input().split())
t = []
for _ in range(n):
    tt = int(input())
    t.append(tt)
t.sort()
ans = deque([])
cnt = 0
for i, tt in enumerate(t):
    if i == 0:
        ans.append([tt+k,1])
        cnt += 1
    else:
        flg = False
        for i in range(len(ans)):
            tmp = ans.popleft()
            if tmp[0] < tt or tmp[1] == c:

                continue
            else:
                flg = True
                break
        if flg :
            tmp[1] += 1
            if tmp[1] != c:
                ans.appendleft(tmp)
        else:
            tmp = [tt+k,1]
            ans.append(tmp)
            cnt += 1
print(cnt)
