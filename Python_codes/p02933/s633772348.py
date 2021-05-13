def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

a = int(input())
s = input()

print(s if a >= 3200 else "red")