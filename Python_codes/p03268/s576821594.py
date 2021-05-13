import sys
def main():
    input = sys.stdin.readline
    N,K=map(int, input().split())
    z=h=0
    for i in range(1,N+1):
        if i%K==0:
            z+=1
        elif K&1==0 and i%K==K>>1:
            h+=1
    ans=z**3
    ans+=h**3
    print(ans)

if __name__ == '__main__':
    main()