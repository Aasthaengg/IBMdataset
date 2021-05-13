import math
A,B,C = map(int,input().split())
ns = sorted([A,B,C])
diff32 = ns[2]-ns[1]
diff21 = ns[1]-ns[0]
ans = diff32+math.ceil(diff21/2)
if diff21 % 2 == 1:
    ans += 1
print(ans)
