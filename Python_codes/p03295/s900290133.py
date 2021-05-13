def main():
    N, M = map(int, input().split())
    l = []
    for _ in range(M):
        a, b = map(int, input().split())
        l.append((a,b))
    l.sort(key=lambda x: x[1])
    r = 0
    p = 0
    for i, j in l:
        if p <= i:
            p = j
            r += 1 
    print(r)
main()
