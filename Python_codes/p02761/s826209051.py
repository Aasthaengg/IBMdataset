n, m = map(int, input().split())
sc_lst = [list(map(int, input().split())) for _ in range(m)]
lst = [0] * n
switch_lst = [0] * n

flag = False

if n == 1:
    lst = [0]
    switch_lst = [0]

    for i in range(m):
        s = 0
        c = sc_lst[i][1]

        if switch_lst[0] == 1:
            if c != lst[0]:
                flag = True
                break
        else:
            lst[0] = c
            switch_lst[0] = 1


else:
    flag = False
    for i in range(m):
        s = sc_lst[i][0] - 1
        c = sc_lst[i][1]

        if switch_lst[s] == 1:
            if lst[s] != c:
                flag = True
                break
            else:
                pass

        else:
            switch_lst[s] = 1
            lst[s] = c

            if s == 0 and c == 0:
                flag = True
                break


if flag:
    answer = -1
else:
    answer = ''
    for i in range(n):
        if switch_lst[i] == 1:
            answer += str(lst[i])
        else:
            if n == 1:
                answer = 0
            else:
                if i == 0:
                    answer += str(1)
                else:
                    answer += str(0)


print(answer)