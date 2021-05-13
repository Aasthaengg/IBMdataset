n = int(input())
s = input()
t = input()

cnt = 0
for i in range(n):
  for j in range(n-i):
    if not s[i+j] == t[j]:
      break
  else:
    print(i+n)
    exit()

else:
  print(2*n)