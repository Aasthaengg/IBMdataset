import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def get_min_without_0(A):
    A = [a for a in A if a != 0]
    return min(A)


def attack(A):
    a = get_min_without_0(A)
    A.remove(a)
    return list(map(lambda x: x % a, A)) + [a]


def check(A):
    cnt = 0
    for a in A:
        if a == 0:
            cnt += 1
    if cnt == len(A) - 1:
        return False
    else:
        return True


def main():
    n = ni()
    A = nl()

    while check(A):
        A = attack(A)
    print(max(A))


if __name__ == '__main__':
    main()
