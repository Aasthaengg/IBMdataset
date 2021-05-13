n,m = map(int, input().split(" "))
a=[list(map(str, input().split(" "))) for i in range(m)]
check = [False for i in range(n + 1)]
times = [False for i in range(n + 1)]

for i in range(m):
  #print(check)
  #print(a[i])
  if check[(int)(a[i][0])] == False and a[i][1] == "AC":
    #print("OK")
    check[(int)(a[i][0])] = True
  elif check[(int)(a[i][0])] == False and a[i][1] == "WA":
    times[(int)(a[i][0])] += 1
    #print("MISS")

for i in range(n + 1):
  if check[i] == False:
    times[i] = 0
print(check.count(True), sum(times))