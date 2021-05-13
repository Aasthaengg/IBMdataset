a=input()
for i in range(len(a)):
    if a[i]=='A':
        n=i
        break
for i in reversed(range(len(a))):
    if a[i]=='Z':
        m=i
        break
print(m-n+1)
