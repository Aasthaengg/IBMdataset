import sys
def main():
    input = sys.stdin.readline
    N,M=map(int, input().split())
    AB=[tuple(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x:x[1])
    ans=0
    pre=-1
    for a,b in AB:
        if pre<=a:
            ans+=1
            pre=b
    print(ans)

if __name__ == '__main__':
    main()