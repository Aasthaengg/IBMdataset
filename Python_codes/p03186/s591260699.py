A, B, C = map(int, input().split())

if C - A >= 0:
    ans = A
    C -= A
else:
    ans = B + C
    print (ans)
    exit()

if C - B >= 1:
    ans += 2 * B + 1
elif C == B:
    ans += 2 * C
else:
    ans += B + C

print (ans)