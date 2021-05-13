A, B = map(int, input().split())
if A > B: A, B = B, A
if (B - A) & 1:
    print('IMPOSSIBLE')
    exit()
print(A + (B - A) // 2)
