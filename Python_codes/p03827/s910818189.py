N = int(input())
S = input()
List = list(S)
x=0
res = 0
for i in range(N):
  if List[i] == "I":
    x += 1
  else:
    x += -1
  res = max(res, x)
print(res)