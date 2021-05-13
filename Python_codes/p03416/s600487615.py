A,B = map(int,input().split())
ans = 0
for i in range(A,B+1):
  temp = list(str(i))
  temp.reverse()
  temp = "".join(temp)
  temp = int(temp)
  if i == temp:
    ans += 1
print(ans)