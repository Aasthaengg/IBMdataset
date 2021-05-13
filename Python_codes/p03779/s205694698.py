def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

X = INT()
i = 1
place = 0

while place < X:
    place += i
    i += 1

ans = i - 1
print(ans)