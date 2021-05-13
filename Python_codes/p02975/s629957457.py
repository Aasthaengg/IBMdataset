def main():
    N = int(input())
    a = list(map(int,input().split()))
    a_set = set(a)
    if len(a_set) > 3:
        return('No')

    if len(a_set) == 1:
        if sum(a_set) == 0:
            return('Yes')
        else:
            return('No')

    elif len(a_set) == 2:
        a_1,a_2 = sorted(a_set)
        if a_1 == 0 and a.count(a_1)*3 == N:
            return ('Yes')
        else:
            return('No')

    else:
        a_1,a_2,a_3 = a_set
        if a.count(a_1) == a.count(a_2) and a.count(a_1) == a.count(a_3) and a.count(a_3) == a.count(a_2):
            if a_1^a_2 == a_3:
                return ('Yes')
            else:
                return('No')
        else:
            return('No')

print(main())
