from string import ascii_lowercase
n = int(input())
S = input()
mod = 10**9 + 7
s = 1
for c in ascii_lowercase:
  s *= S.count(c)+1
  s %= mod
print(s-1)