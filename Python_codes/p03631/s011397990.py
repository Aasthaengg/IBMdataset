n = input()

rev_n = list(n)
rev_n.reverse()
rev_n = "".join(rev_n)

if n == rev_n:
  print('Yes')
else:
  print('No')