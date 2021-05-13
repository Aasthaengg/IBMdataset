import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()

def main():
    N,K=mi()

    if not K <= (N-1)*(N-2)//2:
        print(-1)
        exit()


    k = (N-1)*(N-2)//2
    v = set([(1,x+1) for x in range(1,N)])


    # print(v)

    for i in range(2,N+1):
        for j in range(1,N+1):
            if k <= K: continue

            if i+j <= N and not v in (i,i+j):
                v.add((i,i+j))
                # print((i,i+j))
                k -= 1
            if k <= K:
                break
        if k <= K:
            break



    if k != K:
        print(-1)
        exit()

    print(len(v))
    for x,y in v:
        print(x,y)



if __name__ == "__main__":
  main()