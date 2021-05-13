S = {p:list(input().upper()) for p in 'ABC'}
p = 'A'
while S[p]:
    p = S[p].pop(0)
print(p)
