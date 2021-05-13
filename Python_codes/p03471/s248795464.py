N,Y = map(int,input().split())

x = -1
y = -1
z = -1

if Y <= N*10000 :
  for i in range(N+1):
    for j in range(N-i+1):
      if Y == i*10000 + j*5000 + (N-i-j)*1000:
        x = i
        y = j
        z = N-i-j
        break

print(f"{x} {y} {z}")