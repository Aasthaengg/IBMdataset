a,b,c = map(int, input().split())
if abs(a-b) == c or abs(a-c) == b or abs(b-c) == a:
    print("Yes")
else:
    print("No")