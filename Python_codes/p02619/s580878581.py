#!/usr/bin/env python

def main():
    d = int(input())
    c_lst = list(map(int, input().split()))
    s_mat = [list(map(int, input().split())) for _ in range(d)]

    t_lst = []
    for _ in range(d):
        t_lst.append(int(input())-1)

    scr = 0
    last = [-1 for _ in range(26)]
    for day in range(d):
        t = t_lst[day]
        scr += s_mat[day][t]
        last[t] = day
        for typ in range(26):
            scr -= c_lst[typ] * (day - last[typ])
        print(scr)


if __name__ == '__main__':
    main()
