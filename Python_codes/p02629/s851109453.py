n = int(input())
l = []
alpha = "abcdefghijklmnopqrstuvwxyz"
while n > 0:
  i = (n-1)%26
  l.append(alpha[i])
  n = (n-1)//26
l = l[::-1]
print("".join(l))