def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = list(map(int, input().split()))
        a = [i-1 for i in a]
        a.reverse()
        A.append(a)
    t = N * (N - 1) / 2
    d = 0
    n = set(range(N))
    while True:
        p = 0
        l = set()
        d += 1
        for i in n:
            if A[i] == [] or i in l:
                continue
            j = A[i][-1]
            if A[i][-1] not in l and A[j][-1] == i:
                l.add(i)
                l.add(A[i][-1])
                A[j].pop() 
                A[i].pop()
                t -= 1
                p += 1
        n = l
        if t == 0:
            print(d)
            break
        if p == 0:
            print(-1)
            break
main()
