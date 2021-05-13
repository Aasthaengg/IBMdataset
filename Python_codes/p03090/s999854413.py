
def main():
    N = int(input())
    #N = 5
    a = N - N%2 - 1
    ans = []
    for i in range(N-1):
        for t in range(i+1,N):
            if i+t != a:
                ans += [{i+1,t+1}]
    
    print(len(ans))
    print('\n'.join("{} {}".format(i,t) for i,t in ans))

main()
