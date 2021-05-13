N, K = map(int, input().split())
l = input().split()
l2 = [int(i) for i in l]

line1, line2 = 0, 10**9

while (line2-line1 > 1):
  x = int((line1 + line2) / 2)
  def f(x):
    now = 0
    for i in range(N):
      now += int((l2[i]-1)/x)
    return now <= K
  if f(x)==True:
    line2 = x
  else:
    line1 = x
    
print(line2)