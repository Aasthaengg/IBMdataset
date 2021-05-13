import fileinput

for line in fileinput.input():
    tokens = list(map(int, line.strip().split()))
    a, b = tokens[0], tokens[1]

#data = input().split()
#a, b = data[0], data[1]

if a < b:
    print("a < b")
elif a > b:
    print("a > b")
elif a == b:
    print("a == b")