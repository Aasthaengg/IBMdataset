import collections

def main():
    n,m = tuple([int(t)for t in input().split()])

    a = tuple([int(t)for t in input().split()])

    csum = list(map(lambda a: a%m,cumsum(a)))

    c = collections.Counter(csum)
    ans = 0
    for c_i in c.values():
        ans += c_i*(c_i-1)//2
    print(ans)

def cumsum(a):
    s = 0
    sums = [0]
    for a_i in a:
        s+=a_i
        sums.append(s)

    return sums

if __name__ == "__main__":
    main()