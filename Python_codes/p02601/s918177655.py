R, G, B = list(map(int, input().split()))
K = int(input())

while G <= R and K > 0:
    G *= 2
    K -= 1
while B <= G and K > 0:
    B *= 2
    K -= 1
if B > G > R:
    print("Yes")
else:
    print("No")
