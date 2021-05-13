import math
import copy


def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    p_order = 1
    q_order = 1

    p_diff = []
    q_diff = []
    p_sort = list(range(1, 9))
    q_sort = list(range(1, 9))

    for i in range(n):
        # 残っている要素の下から何番目かを順番に特定する
        p_diff.append(p_sort.index(p[i]))
        q_diff.append(q_sort.index(q[i]))
        p_sort.remove(p[i])
        q_sort.remove(q[i])

    for i in range(n):
        rest_p = len(p_diff[i+1:]) if i < n else 0
        rest_q = len(q_diff[i+1:]) if i < n else 0
        p_order += p_diff[i] * math.factorial(rest_p)
        q_order += q_diff[i] * math.factorial(rest_q)

    answer = abs(p_order - q_order)
    print(answer)


'''
    while p != []:
        i = 0
        diff = p[i] - min(p)
        if diff > 2:
            p_order += math.factorial(len(p) - 1)
        p.pop(i)
'''

'''
    pq_diff = [p[i] - q[i] for i in range(n)]

    answer = 0
    for i in range(n):
        if pq_diff[i] == 0:
            continue
        answer += (pq_diff[i] - 1) * math.factorial(n-i-1)
    print(answer
'''


if __name__ == "__main__":
    main()
