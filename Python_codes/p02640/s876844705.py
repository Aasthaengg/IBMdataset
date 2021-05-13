l = input().split()
x = l[0]
y = int(l[1])

ans = 0

foots = 2*int(x)

for i in  range(int(x)+1):
    if foots == y:
        ans +=1
    foots += 2

if ans == 1:
    print("Yes")

else:
    print("No")