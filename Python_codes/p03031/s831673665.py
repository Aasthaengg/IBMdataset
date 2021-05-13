N, M = map(int, input().split())
ks = []
for i in range(M):
  tmp = list(map(int, input().split()))
  ks.append(tmp)
p = list(map(int, input().split()))

total = 0
for i in range(int(2**N)):
  bin_val = bin(i)				# 2進数に変換
  bin_val = str(bin_val[2:])	# 先頭２文字を除外し、文字列に変換
  bin_val = bin_val.zfill(N)	# N桁になるように先頭に0を追加
#  print(bin_val)
  
  flag = 1
  for j in range(M):
    count = 0
    k = ks[j][0]
    s = ks[j][1:k+1]
    for l in range(k):      
      if bin_val[s[l]-1] == '1':
        count += 1
    if count % 2 != p[j]:
      flag = 0
      break
  if flag == 1:
    total += 1
print(total)

