l = input().split()
l = list(map(int, l))

if l[0] < l[1] and l[1] < l[2]:
    print("Yes")

else:
    print("No")