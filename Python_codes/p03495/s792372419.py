import collections
def solve(n, k, a_list):

    counter = collections.Counter()

    for i in a_list:
        counter[i] += 1

    key_num = len(counter.keys())
    if key_num > k:
        tmp = sorted(counter.items(), key=lambda x: x[1])
        ans = sum([v for k, v in tmp[: key_num - k]])
    else:
        ans = 0

    return ans

if __name__ == "__main__":
    n, k = [int(i) for i in input().split()]
    a_list = [int(i) for i in input().split()]
    print(solve(n, k, a_list))
