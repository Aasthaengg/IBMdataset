import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,M = LI()

    d = {}
    m = M
    for i in range(2,int(math.sqrt(M))+1):
        while m % i == 0:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            m //= i
    if m > 1:
        d[m] = 1

    a = [1]
    b = [1]
    c = 1
    for i in range(1,N+int(math.log(M,2)) +1):
        c = (c * i) % MOD
        a.append(c)
        b.append(pow(c,MOD-2,MOD))

    ans = 1
    for v in d.values():
        ans = (ans * a[N+v-1] * b[v]* b[N-1]) % MOD
    print(ans)

if __name__ == '__main__':
    main()