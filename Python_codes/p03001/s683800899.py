W, H, x, y = map(int, input().split())
s = 0
if W == 2*x and H == 2*y:
  s = 1
S = W*H/2
print(S, s, sep =' ')