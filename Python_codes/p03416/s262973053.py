A,B = map(int,input().split())
count = 0
for i in range(A,B+1):
  i = str(i)
  num = 1
  if len(i)%2 == 0:
    num = 0
  left = i[:len(i)//2]
  right = i[len(i)//2+num:]
  right = right[::-1]
  if left == right:
    count += 1
print(count)