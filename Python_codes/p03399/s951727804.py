a = int(input()) 
b = int(input())
c = int(input())
d = int(input())

total = 0
if a == b:
    total+=a
elif a < b:
    total+=a
else:
    total+=b

if c == d:
    total+=c
elif c < d:
    total+=c
else:
    total+=d

print(total)