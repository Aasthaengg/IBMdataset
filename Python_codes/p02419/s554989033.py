a=0
b=input()
b=b.lower()
while True:
    z=list(map(str,input().split()))
    if z==['END_OF_TEXT']:
        break
    z=[str(i).lower() for i in z ]
    a+=z.count(b)
print(a)