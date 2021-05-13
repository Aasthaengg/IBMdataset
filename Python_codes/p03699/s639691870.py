N = int(input())
total = [int(input()) for i in range(N)]
non = []
for i in range(N):
  if total[i] % 10 != 0:
    non.append(total[i])
if len(non):
  if sum(total) %10 != 0:
    ans = sum(total)
  else:
    ans = sum(total)-min(non)
else:
  ans = 0
print(ans)

    
