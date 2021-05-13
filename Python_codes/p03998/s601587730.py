D = {s:list(input()) for s in "abc"}
p = "a"

while D[p]:
    p=D[p].pop(0)

print(p.upper())