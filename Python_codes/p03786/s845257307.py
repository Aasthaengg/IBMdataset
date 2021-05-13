import itertools
def main():
    n=int(input())
    a=sorted(map(int,input().split()))
    b=list(itertools.accumulate(a))
    cnt=0
    for i in reversed(range(1, n)):
        if b[i-1]*2 < a[i]:
            return n-i
    return n
            
if __name__ == "__main__":
    print(main())