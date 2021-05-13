import sys
arr_S = []
S = str(input())

for i in range(0,len(S)):
  arr_S.append(S[i])
for i in range(0,-1+len(S)):
  if sorted(arr_S)[i+1] == sorted(arr_S)[i]:
    print("no")
    sys.exit()
print("yes")