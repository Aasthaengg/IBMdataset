from sys import stdin
data = stdin.readline().strip()

a = data.split()[0]

if a == "ABC":
    print("ARC")
elif a == "ARC":
    print("ABC")