n = int(input())
a_lst = input().split()
odd = [a for i, a in enumerate(a_lst) if i % 2 != 0]
even = [a for i, a in enumerate(a_lst) if i % 2 == 0]

if n % 2 == 0:
  b = list(reversed(odd)) + even
else:
  b = list(reversed(even)) + odd
print(' '.join(b))