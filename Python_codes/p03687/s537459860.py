s = input();
a = "abcdefghijklmnopqrstuvwxyz"
b = [0]*26
c = [0]*26
for i in s:
  for j in range(26):
    if i == a[j]:
      c[j] = max(c[j],b[j])
      b[j] = 0
    else:
      b[j] += 1
print(min([max(i,j) for i,j in zip(b,c)]))