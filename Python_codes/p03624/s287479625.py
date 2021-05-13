s=input()
alpha="abcdefghijklmnopqrstuvwxyz"
res="None"
for i in alpha:
    if not i in s:
        res=i
        break
print(res)