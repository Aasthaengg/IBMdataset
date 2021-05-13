N = int(input())
H = list(map(int, input().split()))
t = 1
for h in H:
    if t < h:
        t = h-1
    elif t == h:
        pass
    else:
        print("No")
        exit()
print("Yes")
