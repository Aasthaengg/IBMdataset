n = int(input())
for i in range(n):
    p = int(input())
    if not p%2:
        if p != 2:
            n -= 1
        continue
    for j in range(3,int(p**0.5)+1,2):
        if not p%j:
            n -= 1
            break
print(n)