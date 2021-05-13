s = input()
a = s.count("a")==1
b = s.count("b")==1
c = s.count("c")==1

print("Yes" if all([a, b, c]) else "No")