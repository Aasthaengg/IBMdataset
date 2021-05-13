import collections
def slove(n, a):

    count = collections.Counter()
    a_list = [int(i) for i in a.split()]
    for i in a_list:
        count[i] += 1

    tmp = sorted([item for item in count.items() if item[1] >= 2])

    if len(tmp) == 0:
        return 0
    else:
        x = tmp.pop()
        if x[1] >= 4:
            return x[0] ** 2
        else:
            y = tmp.pop()[0]
            return x[0] * y

if __name__ == "__main__":
    n = int(input())
    a_list = input()
    print(slove(n, a_list))
