def main():
    n, m = map(int, input().split())
    ps_lst = [list(map(str, input().split())) for _ in range(m)]
    judge_lst = [0] * n
    penalty_lst = [0] * n
    correct = 0
    penalty = 0

    for i in range(m):
        problem = int(ps_lst[i][0]) - 1
        result = ps_lst[i][1]
        
        if judge_lst[problem] == 0:
            if result == 'AC':
                judge_lst[problem] = 1
            else:
                penalty_lst[problem] += 1

    for i in range(n):
        if judge_lst[i] == 1:
            correct += 1
            penalty += penalty_lst[i]
            
    print(correct, penalty)


if __name__ == '__main__':
    main()