def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

ABCDE = [[INT()] for i in range(5)]

for i in range(5):
    if ABCDE[i][0] % 10 == 0:
        ABCDE[i].append(ABCDE[i][0])
        ABCDE[i].append(0)
        
    else:
        wait = ((ABCDE[i][0] // 10) + 1) * 10
        ABCDE[i].append(wait)
        ABCDE[i].append(wait - ABCDE[i][0])

ABCDE.sort(key = lambda x : x[2])

ans = ABCDE[4][0]

for i in range(4):
    ans += ABCDE[i][1]
    
print(ans)