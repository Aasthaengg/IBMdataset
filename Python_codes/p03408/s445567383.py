def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    s = [input() for _ in range(N)]
    M = ii()
    t = [input() for _ in range(M)]
    dic = {}
    for v in s:
        if not v in dic:
            dic[v] = 0
        dic[v] += 1
    for v in t:
        if not v in dic:
            dic[v] = 0
        dic[v] -= 1

    print(max(0, max(dic.values())))

if __name__ == '__main__':
    main()