import collections
def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = collections.Counter(a)
    num = len(set(a))
    aset=set(a)

    if sum(a) == 0:
        print('Yes')
        return
    # if n % 3 != 0:
        # print('No')
        # return
    if len(cnt.most_common()) == 3:
        a1, a2, a3 = aset
        if cnt.most_common()[0][1] == cnt.most_common()[1][1] == cnt.most_common()[2][1]  and a1 ^ a2 == a3:
            # print(cnt.most_common())
            print('Yes')
            return

    if len(cnt.most_common()) == 2:

        tmp_min = cnt.most_common()[1][1]
        tmp_max = cnt.most_common()[0][1]
        if 3 * tmp_min == n and int(cnt.most_common()[1][0]) == 0:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()
