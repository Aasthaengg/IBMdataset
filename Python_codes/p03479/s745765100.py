def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

X, Y = MI()
ans = 0

while Y >= X:
    X *= 2
    ans += 1
    
print(ans)