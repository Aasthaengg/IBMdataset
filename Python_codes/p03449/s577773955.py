import itertools
def solve(n, a1_list, a2_list):

    a1_acc = itertools.accumulate(a1_list)
    a2_acc = reversed(list(itertools.accumulate(reversed(a2_list))))

    ans = max([i + j for i, j in zip(a1_acc, a2_acc)])

    return ans

if __name__ == "__main__":
    n = int(input())
    a1_list = [int(i) for i in input().split()]
    a2_list = [int(i) for i in input().split()]
    print(solve(n, a1_list, a2_list))
