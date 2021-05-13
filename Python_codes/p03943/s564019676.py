a, b, c = map(int,input().split())
d = [a, b, c]
if (a + b + c) / 2 == max(d):
    print("Yes")
else:
    print("No")