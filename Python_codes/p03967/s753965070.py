s = input()
N = len(s)

g = 0
p = 0
score = 0

for i in range(N):
    if(g > p):
        if(s[i] == "g"):
            p += 1
            score += 1
        else:
            p += 1
    elif(g == p):
        if(s[i] == "g"):
            g += 1
        else:
            g += 1
            score -= 1
print(score) 