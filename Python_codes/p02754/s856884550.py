N, A, B = map(int, input().split())
g = A + B
ct = N // g
cr = N % g
ct = A * ct
if cr > A:
    print(ct + A)
    exit()
print(ct + cr)