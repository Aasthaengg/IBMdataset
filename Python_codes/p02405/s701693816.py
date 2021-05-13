Flag = True
data = []
while Flag:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        Flag = False
    else:
      data.append((H, W))

for (H, W) in data:
    for i in range(H):
        if W % 2 == 0:
            if i % 2 == 0:
                print('#.' * int(W/2))
            else:
                print('.#' * int(W/2))
        else:
            if i % 2 == 0:
                s = '#.' * int((W+1)/2)
                print(s[:-1])
            else:
                s = '.#' * int((W+1)/2)
                print(s[:-1])
    print('\n', end="")
