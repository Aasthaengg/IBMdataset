c11, c12, c13 = map(int, input().split())
c21, c22, c23 = map(int, input().split())
c31, c32, c33 = map(int, input().split())
ans = 'No'
if c11 - c21 == c12 - c22 & c12 - c22 == c13 - c23:
    if c21 - c31 == c22 - c32 & c22 - c32 == c23 - c33:
        if c11 - c12 == c21 - c22 & c21 -c22 == c31 - c32:
            if c12 - c13 == c22 - c23 & c22 - c23 == c32 - c33:
                ans = 'Yes'
print(ans)