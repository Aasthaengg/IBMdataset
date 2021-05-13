a = input()
z = list(a)
d = 0
for i in range(len(z)-1):
    if a[i]!=a[i+1]:
        d +=1
print(d)