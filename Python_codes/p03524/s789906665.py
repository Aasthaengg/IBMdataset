s = input()

a = s.count("a")
b = s.count("b")
c = s.count("c")

check = min(a,b,c) + 1

if check  < a or check  < b or check  < c:
    print("NO")
else:
    print("YES")