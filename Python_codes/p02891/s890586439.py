S = input()
K = int(input())
oans = 0
head = 0
tail = 0
N = len(S)
count = 1

if S.count(S[0]) == N:
  print(N*K//2)
  exit()
for i in range(N-1):
  if S[i+1] == S[i]:
    count += 1
  else:
    oans += count // 2
    if head == 0:
      head = count
    count = 1
  if i == N-2:
    oans += count // 2
    tail = count
    if head == 0:
      print(N*K//2)
      exit()
plus = 0

if S[0] != S[-1]:
  print(oans * K)
  exit()

d = head//2 + tail //2 -(head + tail)//2

print(oans*K -(K-1)*d)