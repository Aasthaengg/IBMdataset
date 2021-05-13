N = int(input())

ans = []
# 偶数だったら対角、奇数だったらその一つ左を引く
for i in range(1, N + 1):
  for j in range(1, N + 1):
    if N % 2 == 0:
      if i != j and i + j != N + 1:
        if [j, i] not in ans:
          ans.append([i, j])
    else:
      if i != j and i + j != N:
        if [j, i] not in ans:
          ans.append([i, j])
print(len(ans))
for i, j in ans:
  print(i, j)