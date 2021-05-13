import collections
def main():
    n,k=map(int, input().split())
    A=[int(i) for i in input().split()]
    dd = collections.defaultdict(int)
    for i in A:
        dd[i]+=1
    res = []

    for i in dd.keys():
        res.append([i,dd[i]])

    res.sort(key = lambda x:x[1])
    type = len(res)
    result = 0
    i=0
    while(type > k):
        result += res[i][1]
        type-=1
        i+=1

    print(result)


if __name__ == '__main__':
    main()
