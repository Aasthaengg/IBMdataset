
def LinearSearch(n, S, t):
    """ ????????????????????¢????????? """
    S.append(t)
    i = 0

    while S[i] != t:
        i += 1

    if i == n:
        return -1
    else:
        return i

n = int(input())
S = [int(s) for s in input().split()]

q = int(input())
T = [int(t) for t in input().split()]

cnt = 0

for t in T:
    if LinearSearch(n, S[:], t) != -1:
        cnt += 1

print(cnt)