a, b = list(input().rstrip().split())
ar = a * int(b)
br = b * int(a)
r = ar if ar < br else br
print(r)

