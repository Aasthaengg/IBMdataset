def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

A, B, C, D = MI()

print(max(A * B, C * D))