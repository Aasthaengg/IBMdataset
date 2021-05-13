def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

A, B, C = MI()
print("Yes" if A <= C <= B else "No")