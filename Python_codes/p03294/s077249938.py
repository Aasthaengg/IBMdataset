def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N = int(input())
a = LI()
f = sum(a) - N

print(f)