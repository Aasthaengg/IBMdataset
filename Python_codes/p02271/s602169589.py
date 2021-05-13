import itertools


def rev(x):
    return sumA - x


if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    M = list(map(int, input().split()))
    sumA = sum(A)
    all_sum = set()
    for i in range((n+1)//2):
        com = set(itertools.combinations(A, i+1))
        com_sum = set(map(sum, com))
        com_sum_rev = set(map(rev, com_sum))
        all_sum = all_sum.union(com_sum)
        all_sum = all_sum.union(com_sum_rev)
    for m in M:
        if m in all_sum:
            print("yes")
        else:
            print("no")