N,C,K = map(int,input().split())
T = [int(input()) for _ in range(N)]


T = sorted(T)

num  = 0  
bus = 0
flag = 0

if C != 1:
  
  for n in range(N):
    if flag == 0:
      person_limit = C-1
      time_limit = T[n] + K
      flag = 1
    else:
      if T[n] <= time_limit:
        person_limit -= 1
        if person_limit == 0:
          bus += 1
          flag = 0
      else:
        bus += 1
        person_limit = C-1
        time_limit = T[n] + K
        flag = 1

    if n == N-1 and flag == 1:
      bus += 1

else:
  bus = len(T)

print(bus)