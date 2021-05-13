a, b, c = map(int, input().split())
if a <= c <= b:
    print("Yes")
    raise SystemExit(0)
print("No")
