import math

A, B, H, M = map(int, input().split())

# for one minute
A_deg=H*(360/12) + M*(360/12/60)
B_deg=M*(360/60)
deg=abs(A_deg-B_deg)

ans = math.sqrt(
  A**2+
  B**2-
  2*A*B*math.cos(math.radians(deg))
)

print(ans)
