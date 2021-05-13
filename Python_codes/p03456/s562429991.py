[a,b] = list(map(str,input().split()))

dam = a+b
dam = int(dam)

out='No'
for i in range(10**5):
    if i**2==dam:
        out='Yes'

print(out)
