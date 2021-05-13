a, b, c = map(int, input().split())
k = int(input())

if max(a,b,c) == a:
    ans = b + c + a*(2**k)
elif max(a,b,c) == b:
    ans = a + c + b*(2**k)
elif max(a,b,c) == c:
    ans = a + b + c*(2**k)

print(ans)
