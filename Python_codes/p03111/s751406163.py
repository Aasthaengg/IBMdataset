from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

n,a,b,c = map(int,input().split())
l = [int(input()) for _ in range(n)]

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

min_mp = 10**10

for i in range(4**n):
    mp = 0
    li = [0]*4
    count_li = [0]*4
    s = Base_10_to_n(i,4).zfill(n)

    for j,k in enumerate(s):
        li[int(k)] += l[j]
        count_li[int(k)] += 1

    if 0 in li[:-1]:
        continue

    mp += abs(a-li[0])
    mp += abs(b-li[1])
    mp += abs(c-li[2])

    for item in count_li[:3]:
        if item >= 2:
            mp += 10*(item-1)
            
    min_mp = min(min_mp,mp)

print(min_mp)