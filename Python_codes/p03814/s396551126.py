s = list(str(input()))

front = s.index("A")
s.reverse()
back = s.index("Z")

print(len(s)-front-back)
