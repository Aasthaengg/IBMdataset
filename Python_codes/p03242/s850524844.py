n = input()
print(*[1 if a=='9' else 9 for a in n], sep="")