import sys

sys.setrecursionlimit(10**7)
strlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def dfs(n, before):
    lensetbefore = len(set(before))
    if n == 1:
        print(before)
    if n > 1:
        for s in strlist[:lensetbefore+1]:
            dfs(n-1, before+s)

def main():
    N = int(input())
    dfs(N, 'a')


if __name__ == "__main__":
    main()
