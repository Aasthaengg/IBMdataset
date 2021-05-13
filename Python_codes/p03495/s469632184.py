import collections
def solve(n, k, a_list):

    counter = collections.Counter()

    for i in a_list:
        counter[i] += 1

    tmp = sorted(counter.values(), reverse=True)
    ans = n - sum(tmp[:k])
    
    return ans

if __name__ == "__main__":
    n, k = [int(i) for i in input().split()]
    a_list = [int(i) for i in input().split()]
    print(solve(n, k, a_list))