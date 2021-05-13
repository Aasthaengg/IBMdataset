import sys
input = sys.stdin.buffer.readline

def main():
    H,W,K = map(int,input().split())
    fib = [1,1,2,3,5,8,13,21,34]
    MOD = 10**9+7
    
    if W == 1:
        print(1)
    else:
        ans = [0 for _ in range(W)]
        ans[0] = 1
        for _ in range(H):
            use = [0 for _ in range(W)]
            for i in range(W):
                if i == 0:
                    use[i] = ans[i]*fib[W-1]+ans[i+1]*fib[W-2]
                elif i == W-1:
                    use[i] = ans[i]*fib[W-1]+ans[i-1]*fib[W-2]
                else:
                    use[i] = ans[i]*fib[i]*fib[W-i-1]+ans[i-1]*fib[i-1]*fib[W-i-1]+ans[i+1]*fib[i]*fib[W-i-2]
                use[i] %= MOD
            ans = use
        print(ans[K-1])
    
if __name__ == "__main__":
    main()
