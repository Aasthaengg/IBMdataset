A, B = map(int, input().split())
count=0

for i in range(A, B+1, 1):
  s = str(i)
  a = int(s[4])
  b = int(s[3])
  c = int(s[1])
  d = int(s[0])
  
  if a==d and b==c:
    count+=1
print(count)