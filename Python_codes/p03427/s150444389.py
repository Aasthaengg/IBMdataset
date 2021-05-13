n=input()
keta=len(n)
a=0
for i in n:
    a+=int(i)
print(max(a,9*(keta-1)+int(n[0])-1))

