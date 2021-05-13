n = int(input())

xu = [0]*n

for i in range(n):
  xu[i] = input().split()
  
ans = []
#print(xu)
for i in range(n):
  if(xu[i][1] == "BTC"):
    ans.append(float(xu[i][0])*380000.0)
  else:
    ans.append(int(xu[i][0]))
print(sum(ans))