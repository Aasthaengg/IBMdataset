N = int(input())
s = list(input())
a = []
for i in range(1, N):
  a.append(len(list(set(s[0:i]) & set(s[i:]))))
print(max(a))