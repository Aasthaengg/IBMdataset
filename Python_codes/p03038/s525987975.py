# input
n, m = map(int, input().split())
data = [[int(i), 1] for i in input().split()]
for i in range(m):
  b, c = map(int, input().split())
  data.append([c, b])
data.sort(key=lambda x:x[0], reverse=True)

# main
ans = 0
cnt = n
for i in range(len(data)):
  if cnt >= data[i][1]:
    ans += data[i][0] * data[i][1]
    cnt -= data[i][1]
  else:
    ans += data[i][0] * cnt
    cnt -= data[i][1]
  if cnt <= 0:
    break
    
# output
print(ans)