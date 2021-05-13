h=input()
b="CODEFESTIVAL2016"
c=0
for i in range(16):
    if h[i]!=b[i]:
        c+=1
print(c)