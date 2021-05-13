a,b = [input() for i in range(2)]
if a[::-1] == b and b[::-1] == a:
    print("YES")
else:
    print("NO")