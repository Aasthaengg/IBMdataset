n = int(input())
s = list(input())
if s.count("R") > n - s.count("R"):
    print("Yes")
else:
    print("No")