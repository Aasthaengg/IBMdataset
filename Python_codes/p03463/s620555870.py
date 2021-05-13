N, A, B = map(int, input().split())

ans = "Alice"
if A % 2 == 0 and B % 2 == 1:
    ans = "Borys"
if A % 2 == 1 and B % 2 == 0:
    ans = "Borys"

print(ans)