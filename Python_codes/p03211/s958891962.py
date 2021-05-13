a=input()
b=[]
for i in range(len(a)-2):
    m=abs(753-int(a[i:i+3]))
    b.append(m)
print(min(b))