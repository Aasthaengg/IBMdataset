A, B = map(int, raw_input().split())
if B % A == 0:
    ans = A + B
else:
    ans = B - A

print str(ans)