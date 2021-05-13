N = int(input())
s = input()
t = input()

for i in range(N):
  for j in range(N - i):
    if s[i + j] != t[j]:
      break
  else:
    print(i + N)
    exit()

print(N * 2)