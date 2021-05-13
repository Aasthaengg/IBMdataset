a = list(input())
if all(i=='9' for i in a[1:]):
    print(9*len(a)-9+int(a[0]))
elif len(a)==1:
    print(a[0])
else:
    print(max(int(a[0])-1, 0)+9*(len(a)-1))