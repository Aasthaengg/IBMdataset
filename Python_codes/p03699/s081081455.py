n = int(input())
s = []
for i in range(n):
  s.append(int(input()))
 
ss = sum(s)
if ss % 10 == 0:
  # sの中で10で割り切れない最小の数を引けば良い
  s.sort()
  m = [t for t in s if t%10!=0]
  if len(m) == 0:
    print(0)
  else:
    print(ss-min(m))
else:
  print(ss)