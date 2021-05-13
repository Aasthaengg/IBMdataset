n = list(input())
l = len(n)

for i in range(l):
    n[i] = int(n[i])

score = 0

if l == 1:
    print(n[0])
else:
    if n.count(9) == l:
        score = sum(n)
    elif n.count(9) == l-1:
        if n[0] != 9:
            score += sum(n)
        else:
            score += 8 + 9*(l-1)
    else:
        if n[0] != 9:
            score += n[0]-1 + 9*(l-1)
        else:
            for j in range(l):
                if n[j] != 9:
                    n[j-1] = 8
                    score += 8 + 9*(l-1)
                    break
    print(score)