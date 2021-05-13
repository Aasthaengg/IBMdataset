import sys
def input():
  return sys.stdin.readline().rstrip()

S=input()
K=int(input())

ichi=0
for i in range(len(S)):
  if S[i]=="1":
    ichi+=1
  else:
    break

print(1 if K<=ichi else S[ichi])
