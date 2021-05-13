def A_A():
    S = input()
    contest = ''
    if S == 'ABC':
        contest = 'ARC'
    elif S == 'ARC':
        contest = 'ABC'
    print(contest)
    return

A_A()