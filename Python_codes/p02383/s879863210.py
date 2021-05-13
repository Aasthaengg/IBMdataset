D = list(map(int, input().split()))
s = input()

for x in range(len(s)):
    if s[x:x+1] == "S":
        temp = D[0]
        D[0] = D[4]
        D[4] = D[5]
        D[5] = D[1]
        D[1] = temp
    elif s[x:x+1] == "W":
        temp = D[0]
        D[0] = D[2]
        D[2] = D[5]
        D[5] = D[3]
        D[3] = temp
    elif s[x:x+1] == "E":
        temp = D[0]
        D[0] = D[3]
        D[3] = D[5]
        D[5] = D[2]
        D[2] = temp
    elif s[x:x+1] == "N":
        temp = D[0]
        D[0] = D[1]
        D[1] = D[5]
        D[5] = D[4]
        D[4] = temp
    
print(D[0])
