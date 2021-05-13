n=int(input())
d=set()
for itr in range(n):
    a=int(input())
    if a in d: d.remove(a)
    else: d.add(a)
print(len(d))