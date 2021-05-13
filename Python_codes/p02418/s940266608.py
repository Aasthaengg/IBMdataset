a = input()
b = input()
c = "No"
for i in range(0,len(a)):
    if len(b) > len(a[i:i+len(b)]):
        n = len(b) - len(a[i:i+len(b)])
        if a[i:i+len(b)] + a[0:n] == b:
            c = "Yes"
    else:
        if a[i:i+len(b)] == b:
            c ="Yes"
print(c)