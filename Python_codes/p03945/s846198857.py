a = input()
d = 0
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        d +=1
print(d)
