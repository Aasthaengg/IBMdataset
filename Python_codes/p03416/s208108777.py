A,B = map(int,input().split())

cnt = 0
for i in range(A,B+1):
  si = str(i)
  checking = si[::-1]
  if si == checking and int(checking) <= B:
    cnt += 1

print(cnt)