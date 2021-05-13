

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    """
    modulos = [0]*2019
    modulos[0] = 1
    S = input()
    base = 1
    num = 0
    for c in S[::-1]:
        num = (base*int(c)+num)%2019
        base = (base*10)%2019
        modulos[num] += 1
    answer = 0
    for n in modulos:
        answer += n*(n-1)//2
    return answer


if __name__ == '__main__':
    print(solve())
