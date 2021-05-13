def li():
    return list(map(int, input().split()))
def mi():
    return map(int, input().split())
def ii():
    return int(input())

N = ii()
S = input()

current = 0
maxx = 0
for s in S:
    if s == "I":
        current += 1
    else:
        current -= 1
    maxx = max(maxx, current)

print(maxx)