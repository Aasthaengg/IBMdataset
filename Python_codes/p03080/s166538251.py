N = int(input())
S = input()

b,r = 0,0
for i in range(N):
  if S[i] == 'B':
    b = b + 1
  else:
    r = r + 1

print('Yes' if r > b else 'No')