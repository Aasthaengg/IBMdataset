from collections import deque

N,C,K = map(int, input().split())

T_list = list() #左がもっとも早く着いた人

for i in range(N):
    T = int(input())
    T_list.append(T)

T_list.sort(reverse=False)

waiting_deque = deque(T_list)
ans = 0

while 1:
    if len(waiting_deque) != 0:
        ans += 1
        bus_passenger = list()
        bus_passenger.append(waiting_deque.popleft())
        while 1:
            if len(waiting_deque)!=0 and len(bus_passenger) < C and bus_passenger[0] + K >= waiting_deque[0]:
                bus_passenger.append(waiting_deque.popleft())
            else:
                #print(bus_passenger)
                break
    else:
        break

print(ans)