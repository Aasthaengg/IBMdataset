n = int(input())
a = list(map(int, input().split()))
m4 = 0
m2 = 0
for i in range(len(a)):
    if (a[i] % 4 == 0):
        m4 += 1
    elif (a[i] % 2 == 0):
        m2 += 1

if (m4*2+m2 >= len(a) or m4*2+1 >= len(a)):
    print("Yes")
else:
    print("No")