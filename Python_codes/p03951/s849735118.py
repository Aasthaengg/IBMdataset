N = int(input())
s = input()
t = input()
for i in range(N):
  if s[i:] == t[:N-i]:
    break
else:
  i += 1
print(2 * i + (N - i))