import collections
def solve(n, s_list):

    counter = collections.Counter()
    for s in s_list:
        counter[s[0]] += 1


    if len(counter.keys()) == 4:
        return "Four"
    else:
        return "Three"


if __name__ == "__main__":
    n = int(input())
    s_list = [i for i in input().split()]
    print(solve(n, s_list))

