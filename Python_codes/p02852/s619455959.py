N, M = map(int, input().split())
S = input()

steps = []
c = N
flg = True
while flg:
    if c <= M:
        steps.append(c)
        break
    
    for i in reversed(range(1, M + 1)):
        if S[c - i] == "0":
            steps.append(i)
            c -= i
            break
        if i == 1:
            steps = [-1]
            flg = False
            
print(*steps[::-1])
