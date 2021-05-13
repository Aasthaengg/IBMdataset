dummy = input().rstrip().split()
a = list(input().rstrip())

if a.count("R") > a.count("B"):
    print("Yes")
else:
    print("No")
