import collections
def solve(n, a_list):

    counter = collections.Counter()

    for i in a_list:
        counter[i] += 1

    ans = sum([v-k if k < v else v for k, v in counter.items() if k != v])

    return ans

if __name__ == "__main__":
    n = int(input())
    a_list = [int(i) for i in input().split()]
    print(solve(n, a_list))