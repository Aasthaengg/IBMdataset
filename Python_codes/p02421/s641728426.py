score1 = score2 = 0
n = int(input())
for _ in range(n):
    s1, s2 = input().split()
    if(s1 > s2): score1 += 3
    elif(s1 < s2): score2 += 3
    else:
        score1 += 1
        score2 += 1
print(score1, score2)