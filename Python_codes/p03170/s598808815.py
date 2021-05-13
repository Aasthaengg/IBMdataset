n,k = map(int, input().split())
a = list(map(int, input().split()))
gru = [0]*(k+1)
for i in range(1,k+1):
  for x in a:
    if i-x >= 0 and gru[i-x] == 0:
      gru[i] = 1
      break
t = ["Second","First"]
print(t[gru[k]])