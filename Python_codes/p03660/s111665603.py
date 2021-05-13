def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    N = int(input())

    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    check = [0] * (N + 1)
    que1 = deque() #fennecのキュー
    que2 = deque() #sunukeのキュー

    que1.append(1)
    que2.append(N)

    check[1] = 1
    check[N] = 1

    fennec = 0
    snuke = 0

    flag = True

    while flag:
        flag = False

        tmp_lst = []
        while len(que1) != 0:
            flag = True
            tmp = que1.popleft()
            for next_ in graph[tmp]:
                if check[next_] == 0:
                    tmp_lst.append(next_)
                    fennec += 1
                    check[next_] = 1
        for i in tmp_lst:
            que1.append(i)
        
        tmp_lst = []
        while len(que2) != 0:
            flag = True
            tmp = que2.popleft()
            for next_ in graph[tmp]:
                if check[next_] == 0:
                    tmp_lst.append(next_)
                    snuke += 1
                    check[next_] = 1
        for i in tmp_lst:
            que2.append(i)

    if fennec > snuke:
        print ('Fennec')
    else:
        print ('Snuke')

if __name__ == '__main__':
    main()