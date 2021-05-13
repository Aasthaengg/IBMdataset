import collections


def resolve():
    S = input()
    counter_S = collections.Counter(S)

    appear_0 = counter_S['0']
    appear_1 = counter_S['1']

    ans = min(appear_0, appear_1) * 2
    print(ans)


resolve()