lst = input().split()

L = int(lst[0])
R = int(lst[1])
d = int(lst[2])

if L % d != 0:
   L = L + d - (L % d)

if R % d != 0:
   R = R - (R % d)

result = int(((R - L) / d) + 1)

print(result)