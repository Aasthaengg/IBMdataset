n = int(input())
a = sorted(list(map(int,input().split())),reverse = True)
c_ls = []
cnt = 0
for i in range(n-1):
  if a[i] == a[i+1]:
    cnt += 1
  else:
    cnt = 0
  if cnt == 3:
    c_ls.append(a[i])
  if (a[i] == a[i+1]) and(a[i] not in c_ls):
    c_ls.append(a[i])
  if len(c_ls) == 2:
    print(c_ls[0]*c_ls[1])
    exit()
print(0)