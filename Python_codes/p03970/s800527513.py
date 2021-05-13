n = input()
a = "CODEFESTIVAL2016"
c = 0
for i in range(len(a)):
    if a[i]!=n[i]:
        c+=1
print(c)