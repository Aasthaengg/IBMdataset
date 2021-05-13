H,W = map(int, input().split())
L = []
while H != 0 or W != 0:
 L.append([H, W])
 H,W = map(int, input().split())

def draw(H,W):
 for i in range(H):
  print("#" * W)
 print("")

for (H, W) in L:
 draw(H,W)