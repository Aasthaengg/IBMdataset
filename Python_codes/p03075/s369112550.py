def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

p = [INT() for i in range(5)]
k = INT()

p.sort()
flg = False

for i in range(5):
    for j in range(i, 5):
        if abs(p[j] - p[i]) > k:
            flg = True
            break
            
print(":(" if flg else "Yay!")