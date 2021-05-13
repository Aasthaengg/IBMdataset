S = input()

max_p = len(S)//2

g,p = 0,0
for s in S:
    if s == 'g':
        g += 1
    else:
        p += 1
# print(g)
# print(p)
#print(max_p)

print(max_p - p)
