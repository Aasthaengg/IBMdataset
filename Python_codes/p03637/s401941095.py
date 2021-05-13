N = int(input())
a = list(map(int, input().split()))

even4, even, odd = 0, 0, 0
for i in a:
    if i % 4 == 0:
        even4 += 1
    elif i % 2 == 0:
        even += 1
    else:
        odd += 1

if N % 2 == 0:
    if even4 >= odd:
        print("Yes")
    else:
        print("No")
else:
    if even4 >= odd - 1:
        print("Yes")
    else:
        print("No")
