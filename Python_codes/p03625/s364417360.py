from collections import Counter
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ac = Counter(a)
    acl = [i for i in ac if ac[i] >= 2]
    acl.sort(reverse=True)

    if len(acl) == 0:
        print(0)
    elif ac[acl[0]] >= 4:
        print(int(acl[0] * acl[0]))
    elif len(acl) <= 1:
        print(0)
    else:
        print(int(acl[0]*acl[1]))

if __name__ == '__main__':
    main()
