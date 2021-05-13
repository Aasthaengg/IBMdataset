def main():
    N = int(input())
    a = list(map(int, input().split()))
    l = []
    if abs(max(a)) >= abs(min(a)):
        i = a.index(max(a))
        t = max(a)
        for j in range(1, N+1):
            l.append((i+1, j))
        for i in range(1, N):
            l.append((i, i+1))
    else:
        i = a.index(min(a))
        t = min(a)
        for j in range(1, N+1):
            l.append((i+1,j))
        for i in range(N-1, 0, -1):
            l.append((i+1, i))
    print(len(l))
    for i in l:
        print(i[0], i[1])
main()
