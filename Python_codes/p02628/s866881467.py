def Qb():
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    f.sort()
    print(sum(f[:k]))

if __name__ == '__main__':
    Qb()
