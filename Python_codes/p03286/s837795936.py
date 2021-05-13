n = int(input())
lst = []

while (n!=0):
    r = int(n%2)
    if(r<0):
        r += 2
    lst.append(r)
    n = (n-r)/(-2)

if len(lst) ==0:
    print("0")
else:
    for i in range(len(lst)):
        print(lst[-1-i],end="")
    print()