import sys
sys.setrecursionlimit(10 ** 8)
n = int(input())
alp = "abcdefghijklmnopqrstuvwxyz"
permutations = []

def dfs(a, size):
    if len(a) == size:
        global permutations
        permutations.append(a)
        return
    for i in range(1, max(a) + 2):
        dfs(a + [i], size)

dfs([1], n)
for i in permutations:
    print(''.join([alp[j-1] for j in i]))