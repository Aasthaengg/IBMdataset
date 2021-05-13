def dfs(s,n,adj):
    adj = 'abcdefghij'
    if len(s) == n:
        print(s)
    else:
        for child in adj[:len(set(s))+1]:
            dfs(s+child,n,adj)
    return -1

def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    adj = 'abcdefghij'
    dfs('a',n,adj)


if __name__ == '__main__':
    main()