import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    max_i = int(math.log2(N))
    div = []
    for i in range(1,int(math.sqrt(N))+1):
        if N % i == 0:
            div.append((i,N//i)); div.append((N//i,i))

    ans = 0
    for a,b in div:
        if a == 1:
            for i in range(1,int(math.sqrt(b-1))+1):
                if (b-1) % i == 0:
                    p = 2 - (i*i == b-1) - (i == 1)
                    ans += p
        else:
            for i in range(1,max_i+1):
                c = round(math.pow(a,1/i))
                if c ** i == a:
                    if b % c == 1: ans += 1
    print(ans)

if __name__ == '__main__':
    main()