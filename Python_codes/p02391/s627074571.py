input = input().strip().split()
a = int(input[0])
b = int(input[1])

def comp(a, b):
        if a>b:
                return "a > b"
        elif a<b:
                return "a < b"
        else:
                return "a == b"

print(comp(a,b))