import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    d = [-1,2,5,5,4,5,6,3,7,6]
    
    keta = [-1]*(N+10)
    keta[0] = 0
    
    for i in range(N):
        for num in a:
            if keta[i] != -1:
                keta[i+d[num]] = keta[i]+1

    use = N
    
    ans = [-1]*(N+10)
    ans[0] = 0
    for i in range(N):
        for num in a:
            if keta[i+d[num]] == keta[i]+1:
                ans[i+d[num]] = max(ans[i+d[num]],ans[i]*10+num)
    
    print(ans[N])
    
if __name__ == "__main__":
    main()
