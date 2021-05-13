#%%
n = int(input())
a = list(input())
b = list(input())
c = list(input())


x=0

for i in range(len(a)):
    tmp = []
    tmp.append(a[i])
    tmp.append(b[i])
    tmp.append(c[i])
 
    d = len(list(set(tmp)))
    if d == 1:
        pass
    elif d == 2:
        x += 1
    else:
        x += 2

print(x)