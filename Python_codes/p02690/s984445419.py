import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    X=ii()

    def is_ok(a,b):
        return a**5 <= X+b**5

    for a in range(-1010,1010):
        l,r = -INF,INF
        while r-l > 1:
            mid = (r+l)//2
            if is_ok(a,mid):
                r = mid
            else:
                l = mid
        b=r
        # print(a,b)
        if a**5-b**5==X:
            print(a,b)
            exit()




if __name__ == "__main__":
    main()