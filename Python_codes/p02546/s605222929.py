a = input()
N = len(a)
if a[N-1]=="s":
    b = a+"es"
else:
    b = a + "s"
print(b)