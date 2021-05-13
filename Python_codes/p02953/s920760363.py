n = int(input())
H = list(map(int, input().split()))
b = -1
for h in H:
    if b > h:
        if b != h+1:
            print("No")
            exit()
        else:
            b = h+1
    else:
        b = h

print("Yes")