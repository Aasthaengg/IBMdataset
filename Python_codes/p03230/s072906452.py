N = int(input())
flag = False
k = 0
if N == 1:
  print('Yes')
  print(2)
  print(1,1)
  print(1,1)
  exit()
for i in range(N+1):
    if i*(i-1)/2 == N:
        flag = True
        k = i
        break
if flag == False:
    print('No')
else:
    L = []
    cnt = 0
    dot = 1
    for j in range(k-1):
        M = []
        while cnt < j+1:
            M.append(dot)
            cnt += 1
            dot += 1
        L.append(M)
        cnt = 0
    ans = []
    for i in range(k-1):
      S = L[i]
      for j in range(i+1,k-1):
        S += [L[j][i]]
      ans.append(S)
    T = []
    for i in range(k-1):
      T.append((i+1)*(i+2)//2)
    ans.append(T)
    print('Yes')
    print(k)
    for i in range(len(ans)):
      ans[i] = [k-1]+ans[i]
      for j in range(len(ans[i])):
        if j != len(ans[i])-1:
          print(ans[i][j],end = ' ')
        else:
          print(ans[i][j],end = '')
      print()