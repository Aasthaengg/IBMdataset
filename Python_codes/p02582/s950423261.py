def rainyseason(S):
    days = 0
    max_days = 0
    flag = 0
    for i in range(len(S)):
        if S[i] == 'R':
            days += 1
            flag = 1
        elif S[i] == 'S' and flag == 1:
            if days > max_days:
                max_days = days
                days = 0
                flag = 0
    if days > max_days:
        max_days = days
    return max_days

if __name__ == '__main__':
    S =str(input())
    print(rainyseason(S))