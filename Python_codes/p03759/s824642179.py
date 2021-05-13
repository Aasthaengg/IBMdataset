import sys
a,b,c = map(int,input().split())
if a < 0 or b < 0 or c < 0 or a > 100 or b > 100 or c > 100:
    sys.exit()

diff_a_b = b - a
diff_b_c = c - b

if diff_a_b == diff_b_c:
    print("YES")
else:
    print("NO")