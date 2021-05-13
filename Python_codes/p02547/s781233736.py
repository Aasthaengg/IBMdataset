N= int(input())
a = [input().split() for i in range(N)]

Is = []
for i in range(N):
    Ds = a[i]
    if Ds[0] == Ds[1]:
        Is.append(i)

Boooo = False
for i in range(len(Is)-2):
    if Is[i]+1 == Is[i+1] and Is[i+1]+1 == Is[i+2]:
        Boooo = True

if Boooo:
    print("Yes")
else:
    print("No")

