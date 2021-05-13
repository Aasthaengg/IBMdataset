def main():
    N, X = map(int, input().split())
    m = []
    for i in range(N):
        m.append(int(input()))
    m.sort()
    t = sum(m)
    q = len(m)
    while t <= X:
        t += m[0]
        q += 1
    print(q-1)
main()