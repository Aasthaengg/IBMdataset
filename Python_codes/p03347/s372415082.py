n = int(input())
A = [int(input()) for _ in range(n)]
ans = 0
prev = 0
if A[0]!=0:
  print(-1)
  exit()
for i in range(n):
    a = A[i]
    if prev == None and a!=0:
        ans = -1
        break
    if prev != None:
        dif = a-prev
        if dif >= 2:
            ans = -1
            break
        elif dif<=0:
            ans += prev
    prev = a
if ans!=-1:
    ans += prev
print(ans)