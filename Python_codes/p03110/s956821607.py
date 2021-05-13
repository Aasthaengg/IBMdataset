n=int(input())
sum = 0
for i in range(n):
  s = input().rstrip().split(' ')
  a=float(s[0])
  b=str(s[1])
  if b == "JPY":
    sum += int(a)
  else:
    sum += float(a)*380000
print(sum)