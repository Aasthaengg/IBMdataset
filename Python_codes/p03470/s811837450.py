N=int(input())
mochi=[]
last=[]
for i in range(N):
  mochi.append(int(input()))
for i in range(N):
  if mochi[i] not in last:
    last.append(mochi[i])
print(str(len(last)))