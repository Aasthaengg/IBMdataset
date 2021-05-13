def abc157c_guess_the_number():
    n, m = map(int, input().split())
    ans = ''
    if n == 1:
        ans = '0'
    if n == 2:
        ans = '10'
    if n == 3:
        ans = '100'
    changed = [False] * n
    for i in range(m):
        s, c = map(int, input().split())
        if ans[s - 1] != str(c):
            if changed[s-1]:
                print('-1')
                return
            ans_lst = list(ans)
            ans_lst[s - 1] = str(c)
            ans = ''.join(ans_lst)
            changed[s - 1] = True
    if n >= 2 and ans[0] == '0':
        print('-1')
        return

    print(int(ans))
abc157c_guess_the_number()