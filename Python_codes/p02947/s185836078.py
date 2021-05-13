import collections
def main4():
    n = int(input())
    l = []
    for i in range(n):
        s = input()
        l.append((sorted(s)))
    l.sort()
    dd = collections.defaultdict(int)
    k = []
    for i in range(n):
        k.append(''.join(l[i]))
    res = 0
    for i in range(n):
        dd[k[i]]+=1
    for i in dd.values():
        res += (i*(i-1))//2
    print(res)

if __name__ == '__main__':
    main4()
