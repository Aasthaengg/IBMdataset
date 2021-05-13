from collections import deque
s = deque(list(input()))   # deque オブジェクトを取得

ans=0
cach=-1
while True:
    if s==deque([]):
        break
    else:
        tmp=s.popleft()

    if tmp != cach:
        ans +=1
        cach=tmp
    else:
        if s!=deque([]):
            tmp+=s.popleft()
            ans +=1
            cach=tmp

print(ans)
