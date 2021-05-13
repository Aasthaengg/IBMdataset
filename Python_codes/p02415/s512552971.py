a = str(input())
for i,b in enumerate(a):
    if b == a[i].upper():
        print(a[i].lower(),end='')
    else:
        print(a[i].upper(),end='')
print()
