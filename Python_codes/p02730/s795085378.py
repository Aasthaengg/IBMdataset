a = str(input())
b = len(a)
c = (b-1)//2
d = (b+3)//2
if a[:(c)] == a[(d-1):]:
    print("Yes")
else:
    print("No")