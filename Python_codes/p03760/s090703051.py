a = input()
b = input()
s = ""
for i in range(len(a)+len(b)):
    s+=a[0]
    a=a[1:]
    a,b=b,a

print(s)