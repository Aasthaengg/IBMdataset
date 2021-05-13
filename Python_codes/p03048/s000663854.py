a, b, c, n = list(map(int, input().split()))

cnt = 0
for i in range(n//a+1):
  an = n - a * i
  for j in range(an//b+1):
    num = an - b * j
    if num >= 0 and num % c == 0:
      cnt+=1
        
print(cnt)