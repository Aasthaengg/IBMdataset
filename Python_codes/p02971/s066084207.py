n = int(input())
an = [int(input()) for _ in range(n)]

check = sorted(an, reverse=True)
for i in range(n):
  if an[i] == check[0] :
    print(check[1])
  else :
    print(check[0])
