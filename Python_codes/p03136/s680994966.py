def actual(n, L):
    max_l = max(L)
    others_l = sum(L) - max_l

    if max_l < others_l:
        return 'Yes'

    return 'No'

n = int(input())
L = list(map(int, input().split()))
print(actual(n, L))