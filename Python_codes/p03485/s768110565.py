[a, b] = list(map(int, input().split()))

if (a+b)%2 == 0:
  ave = (a+b)/2
else:
  ave = (a+b+1)/2

print(int(ave))