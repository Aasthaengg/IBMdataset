a, b, c, d = list(map(int, input().split()))
if abs(a-c) <= d or a == c:
    print("Yes")
elif abs(a-b) <= d and abs(b-c) <= d:
    print("Yes")
elif a == b and b == c:
    print("Yes")
else:
    print("No")