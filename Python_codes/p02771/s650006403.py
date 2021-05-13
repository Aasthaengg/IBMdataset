t = list(map(int, input().split()))
a = t[0]
b = t[1]
c = t[2]

if a != b and b != c and a != c:
    print("No")
elif a == b == c:
    print("No")
else:
    print("Yes")
