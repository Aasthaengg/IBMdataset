a, b, c = [int(elem) for elem in input().split()]
if c <= b:
	print(b + c)
else:
  if (c - b) <= a:
    print(b + c)
  else:
    print(a + 2 * b + 1)