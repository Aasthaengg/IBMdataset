N = int(input())
h0 = 0
for h in map(int, input().split()):
    if h0 < h:
        h0 = h-1
    elif h0 == h:
        continue
    else:
        print("No")
        exit()
print("Yes")
