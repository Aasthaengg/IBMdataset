n=int(input())
d=dict()
for _ in range(n):
    a=int(input())
    if a not in d:
        d[a]=0
    else:
        del d[a]
print(len(list(d)))