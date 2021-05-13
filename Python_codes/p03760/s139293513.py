o=input()
e=input()
res=""
for i in range(len(o)+len(e)):
    if i%2==0:
        res+=o[i//2]
    if i%2==1:
        res+=e[i//2]
print(res)
