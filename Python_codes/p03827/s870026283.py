def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N = INT()
S = input()
x = 0
ans = 0

for s in S:
    if s == "I":
        x += 1
    else:
        x -= 1
        
    ans = max(ans, x)
        
print(ans)