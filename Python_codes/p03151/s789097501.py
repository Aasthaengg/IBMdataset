from collections import deque
N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

AB_list = sorted([A-B for A,B in zip(A_list, B_list)])
AB_q = deque(AB_list)

if sum(AB_list) < 0:
    print(-1)
    exit()
if AB_list[0] >= 0:
    print(0)
    exit()

cnt = 0
stock = 0
while len(AB_q) > 0:
    if stock <= 0:
        stock += AB_q.pop()
    else:
        lv = AB_q.popleft()
        if lv >= 0:
            break
        stock += lv
    cnt += 1
print(cnt)
