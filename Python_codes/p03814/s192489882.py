a = input("")
a_num = a.index("A")
for i in range(len(a)-1,-1,-1):
    if a[i]=="Z":
        z_num = i+1
        break
print(len(a[a_num:z_num]))