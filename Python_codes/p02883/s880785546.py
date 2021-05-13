import sys
sys.setrecursionlimit(10**9)

INF = 10**20
def main():
    N,K = map(int,input().split())
    A=list(map(int,input().split()))
    F=list(map(int,input().split()))

    A.sort()
    F.sort(reverse=True)

    def c(s): # sに対して単調減少
        sum_x = 0
        for i in range(N):
            a,f=A[i],F[i]
            tp = s//f
            if not a <= tp:
                sum_x += a-tp

        return sum_x <= K

    l=-1
    r=10**20
    while r-l>1:
        mid = (l+r)//2
        if c(mid):
            r = mid
        else:
            l = mid

    print(r)

if __name__ == "__main__":
  main()
