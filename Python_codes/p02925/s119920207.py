from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    al = []
    al.append(deque([]))
    for _ in range(n):
        row = list(map(int, input().split()))
        al.append(deque(row))

    # print(al)

    day = 0
    cnt = 0
    max_cnt = n*(n-1)//2
    check_il = [i for i in range(1,n+1)]
    while True:
        next_check_il = check_il[:]
        check_il = []
        day += 1
        already_fights = set()
        update_flag = False
        for i in next_check_il:
            al_i = al[i]
            if not al_i or i in already_fights: continue
            i_next_rival = al_i[0]

            al_rival_i = al[i_next_rival]
            if not al_rival_i or i_next_rival in already_fights: continue
            i_next_rival_rival = al_rival_i[0]

            if i_next_rival_rival == i:
                al[i].popleft()
                al[i_next_rival].popleft()
                already_fights.add(i)
                already_fights.add(i_next_rival)
                check_il.append(i)
                check_il.append(i_next_rival)
                cnt += 1
                update_flag = True
            else:
                continue

        if not update_flag:
            print(-1)
            exit()

        if cnt == max_cnt:
            break

    print(day)


if __name__ == "__main__":
    main()