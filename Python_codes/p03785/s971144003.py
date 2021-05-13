N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]


from collections import deque

T = deque(sorted(T))

t_ref = T[0]

bus = 0
member = 0

while T != deque([]):
    t = T[0]
    if t - t_ref <= K and member < C:
        member += 1
        t_tmp = T.popleft()
#        print(t_tmp, 'ok')
#        print(member)
    else:
        bus += 1
        member = 0
        t_ref = T[0]
#        print()
#        print(t_ref, 'new')
if member > 0:
    bus += 1
#print()
print(bus)
