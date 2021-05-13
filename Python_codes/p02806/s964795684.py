N = int(input())
ST = list()
for _ in range(N):
  ST.append(list(input().split()))

X = input()
time = 0
play = 0
for i in range(N):
  if play==0:
    if play==0 and ST[i][0] == X:
      play = 1
    continue
  time += int(ST[i][1])
  
print(time)