import collections
def main4():
    dd = collections.defaultdict(int)
    n = int(input())
    res = 0
    for i in range(n):
        s = input()
        a = sorted(s)
        dd[''.join(a)]+=1
    for i in dd.values():
        res += (i*(i-1))//2
    print(res)


if __name__ == '__main__':
    main4()