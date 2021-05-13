N = int(input())
Min = 100000
for i in range(1,10):
  Dif = i * 111 - N
  if min(Min,Dif) == Dif and i * 111 >= N:
    ans = i * 111
    Min = Dif
print(ans)