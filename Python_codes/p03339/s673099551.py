n = int(input())
s = input()
wcnt = [0] * (n + 2)
ecnt = [0] * (n + 2)
for i in range(n):
  if s[i] == 'W':
    wcnt[i + 1] = wcnt[i] + 1
  else:
    wcnt[i + 1] = wcnt[i]
for i in range(n):
  if s[-(i + 1)] == 'E':
    ecnt[-(i + 2)] = ecnt[-(i + 1)] + 1
  else:
    ecnt[-(i + 2)] = ecnt[-(i + 1)]
#print(wcnt)
#print(ecnt)
lst = [wcnt[i - 1] + ecnt[i + 1] for i in range(1, n + 1)]
#print(lst)
print(min(lst))