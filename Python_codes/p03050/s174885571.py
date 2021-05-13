import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    N = m*p+q = m*q+q = q*(m+1)   q < m
    N%m = (m*p+q)%m = q%m = q = N/m = (m*p+q)/m = p

    3*2+2
    7*1+1
    """
    N = read_int()
    answer = 0
    for q in range(1, math.ceil(math.sqrt(N))):
        if N%q == 0 and q < N//q-1:
            answer += N//q-1
    return answer



if __name__ == '__main__':
    print(solve())
