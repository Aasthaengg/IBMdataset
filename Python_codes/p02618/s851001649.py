import random
import time
import numpy as np

def decrease(day, schedule, c, s, satisfy):
    ret = 0
    date = [0] * 26

    for d in range(day):
        now = schedule[d] + 1
        date[now - 1] = d + 1
        tmp = 0
        for i in range(26):
            tmp += c[i] * (now - date[i])
        ret += tmp
        satisfy.append(tmp)

    return ret

def change(_from, _to, schedule, c, s, satisfy):
    ret = 0
    date = [0] * 26

    for d in range(_to):
        if d < _from:
            ret += satisfy[d]
            continue

        now = schedule[d] + 1
        date[now - 1] = d + 1
        tmp = 0
        for i in range(26):
            tmp += c[i] * (now - date[i])
        ret += tmp
        satisfy[d] = tmp

    return ret

def Main():
    D = int(input())
    c = list(map(int, input().split()))
    s = [list(map(int, input().split())) for _ in range(D)]
    
    dissatisfy=[]
    schedule = []
    score = 0
    start = time.time()

    #最大値を足すだけ
    for i in range(D):
        schedule.append(np.argmax(s[i]))
        score += np.max(s[i])
    
    ans = score - decrease(D, schedule, c, s, dissatisfy)
    
    while time.time() - start < 1.85:
        contest = random.randint(0, 25)
        day = random.randint(0, D - 1)
        if schedule[day] == contest:
            continue

        save = dissatisfy.copy()
        dec = change(day + 1, D, schedule, c, s, dissatisfy)
        score2 = score - s[day][schedule[day]] + s[day][contest]

        if ans < score2 - dec:
            ans = score2 - dec
            score = score2
            schedule[day] = contest
        else:
            dissatisfy = save
        
    for i in range(D):
        print(schedule[i] + 1)

if __name__ == "__main__":
    Main()