import itertools
import numpy as np


def check_eight(n):
    div_list = []
    for i in range(3, n + 1, 2):
        if n % i == 0:
            while n % i == 0:
                n = n // i
                div_list.append(i)
        if n == 1:
            break

    answer_list = []
    for i in range(1, len(div_list)+1):
        comb = itertools.combinations(div_list, i)
        for c in comb:
            c = np.array(c)
            answer_list.append(c.prod())
    answer = len(set(answer_list)) + 1
    
    return answer == 8

if __name__ == "__main__":
    N = int(input())

    count = 0
    for n in range(1, N + 1, 2):
        count += check_eight(n)

    print(count)