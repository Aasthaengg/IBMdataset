def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b

r = int(input())
g = int(input())

print(2*g-r)