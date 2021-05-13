import collections
def get_ans(strings, n):
    ans = 0
    for i in range(n):
        counter = collections.defaultdict(int)
        for k in strings:
            counter[k[i]] += 1
        ans += len(strings) - max(counter.values())
    return ans

if __name__ == '__main__':
    n = int(input())
    strings = []
    for _ in range(3):
        strings.append(input())
    print(get_ans(strings, n))
