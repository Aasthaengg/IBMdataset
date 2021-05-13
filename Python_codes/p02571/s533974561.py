a = input()
b = input()

T=1000

for i in range(len(a)-len(b)+1):
  ans = 0
  for j in range(len(b)):
    if a[i+j]!=b[j]:
      ans +=1
  T = min(T, ans)
print(T)