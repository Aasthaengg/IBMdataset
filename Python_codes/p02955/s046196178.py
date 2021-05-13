import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,K = LI()
    A = LI()

    s = sum(A)
    d = [s]
    for i in range(2,int(math.sqrt(s))+1):
        if s % i == 0:
            d.append(i)
            if s // i != i:
                d.append(s//i)

    ans = 1
    for x in d:

        B = []
        s = 0
        for y in A:
            c1 = x - y % x
            B.append((c1,y))
            s += c1

        B.sort(reverse=True)
        cnt = 0
        for y,_ in B[s//x:]:
            cnt += y
        if cnt <= K:
            ans = max(ans,x)
    print(ans)

if __name__ == '__main__':
    main()