def main():
    from queue import deque

    K = int(input())
    q = deque()
    for i in range(1, 10):
        q.append(i)
    for i in range(K - 1):
        s = q.popleft()
        for j in range(-1, 2):
            add = (s % 10) + j
            if add >= 0 and add <= 9:
                q.append(s * 10 + add)
    print(q.popleft())


main()
