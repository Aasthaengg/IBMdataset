import sys
import random
test = False

def solve(c_list, days, now):
    r = sum(c_list[i]*(now-days[i]) for i in range(26))
    return r


if test == True:
    #seed = 94
    #random.seed(seed)
    d = 365
    c = [random.randrange(0, 101) for _ in range(26)]
    s = [[random.randrange(0, 20001) for _ in range(26)] for _ in range(d)]
    c_ = ' '.join(map(str, c))
    s_ = '\n'.join([' '.join(map(str, i)) for i in s])
    with open('./input.txt', 'w') as f:
        f.write('\n'.join([str(d), c_, s_]))
else:
    d = int(input())
    c = list(map(int, input().split()))
    s = [list(map(int, input().split())) for _i in range(d)]


last_days = [-1 for _i in range(26)]
result = []
score = 0
for today in range(d):
    checker = [c[j]*(today-last_days[j]) for j in range(26)]
    y = sum(checker)

    finder = [s[today][j]-(y-checker[j]) for j in range(26)]
    x = finder.index(max(finder))

    if today < d-1:
        second_checker = [c[j]*(today+1-last_days[j]) for j in range(26)]
        second_finder = [s[today+1][j]-(y-checker[j]) for j in range(26)]
        second_x = second_finder.index(max(second_finder))
        if x == second_finder:
            x = finder.index(sorted(finder)[-2])
    

    last_days[x] = today
    result.append(x+1)
    score += s[today][x] - solve(c, last_days, today)
if test:
    print(score)

def change(problems, days):
    last_days = [-1 for _i in range(26)]
    score = 0
    for i in range(d):
        score += s[i][problems[i]-1]
        last_days[problems[i]-1] = i
        score -= sum([c[j]*(i-last_days[j]) for j in range(26)])
    return score

change_list = result.copy()
for i in range(500):
    if random.randrange(2)<1:
        x, y = random.randrange(0, d), random.randrange(0, d)
        while x == y:
            y = random.randrange(0, d)
        change_list[x], change_list[y] = change_list[y], change_list[x]
        next_score = change(change_list, d)
        if next_score >= score:
            if test:print(i, score, next_score, abs(next_score-score), 'two')
            score = next_score
            result[x], result[y] = result[y], result[x]
        
        else:
            change_list[x], change_list[y] = change_list[y], change_list[x]
    else:
        x = random.randrange(0, d)
        y = random.randrange(1, 27)
        change_list[x], z = y, change_list[x]
        next_score = change(change_list, d)
        if next_score >= score:
            if test:print(i, score, next_score, abs(next_score-score), 'one')
            score = next_score
            result[x] = y
        else:
            change_list[x] = z

if test == True:
    with open('./output.txt', 'w') as f:
        f.write('\n'.join(map(str, result)))
else:
    for i in result:
        print(i)