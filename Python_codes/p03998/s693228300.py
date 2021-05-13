from collections import deque

SA = deque(input())
SB = deque(input())
SC = deque(input())

NowCard = SA.popleft()
ans = 'A'

while True:
    if NowCard == 'a':
        NowList = SA
        ans = 'A'
    elif NowCard == 'b':
        NowList = SB
        ans = 'B'
    elif NowCard == 'c':
        NowList = SC
        ans = 'C'

    if len(NowList) == 0:
        break

    NowCard = NowList.popleft()

print(ans)
