import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N = int(input())
lst1 = [[0, i] for i in range(10 ** 5  +10)]
lst2 = [[0, i] for i in range(10 ** 5 + 10)]

V = tuple(map(int, input().split()))

for i in range(N):
    if i % 2 == 0:
        lst1[V[i]][0] += 1
    else:
        lst2[V[i]][0] += 1

lst1.sort(key = lambda x: x[0],reverse = True)
lst2.sort(key = lambda x: x[0],reverse = True)

if lst1[0][1] != lst2[0][1]:
    print (N - lst1[0][0] - lst2[0][0])
else:
    print (N - max(lst1[0][0] + lst2[1][0], lst1[1][0] + lst2[0][0]))