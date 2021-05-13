a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

if a[0] - b[0] == a[1] - b[1] == a[2] - b[2]:
    if  b[0] - c[0] == b[1] - c[1] == b[2] - c[2]:
        print("Yes")
        exit()
    else:
        pass

print("No")