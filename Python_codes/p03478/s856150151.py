N,A,B = map(int,input().split())
cnt = 0
for i in range(1,N+1):
  if i<10:
    if A <= i <= B:
      cnt += i
  elif 10 <= i < 100:
    if A <= int(str(i)[0])+int(str(i)[1]) <= B:
      cnt += i
  elif 100 <= i < 1000:
    if A <= int(str(i)[0])+int(str(i)[1])+int(str(i)[2]) <= B:
      cnt += i
  elif 1000 <= i < 10000:
    if A <= int(str(i)[0])+int(str(i)[1])+int(str(i)[2])+int(str(i)[3]) <= B:
      cnt += i
  else:
    if A <= 1 <= B:
      cnt += i
print(cnt)