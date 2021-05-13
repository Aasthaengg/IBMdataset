a,b,c=input().split()
d=[a,b,c]
for i in range(2):
    if d.count(d[i])!=1:
        del d[i]
print(len(d))
