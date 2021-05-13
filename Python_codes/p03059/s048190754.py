def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

A, B, T = MI()

print(B * int((T + 0.5) // A))