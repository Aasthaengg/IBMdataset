s = input()
K = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
inv_alpha = "azyxwvutsrqponmlkjihgfedcb"
D = {inv_alpha[i]: i for i in range(26)}
n = len(s)
for i in range(n):
  if i == n - 1:
    x = K % 26
    print(alpha[(26-D[s[i]]+x)%26], end = '')
  else:
    if K >= D[s[i]]:
      K -= D[s[i]]
      print('a', end = '')
    else:
      print(s[i], end = '')
print()