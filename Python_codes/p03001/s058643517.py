W, H, x, y = list(map(lambda n: int(n), input().split(" ")))
 
S = W * H / 2

print(S, end=" ")
print(1) if W == 2 * x and H == 2 * y else print(0)