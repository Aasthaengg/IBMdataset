def main():
    n,m = map(int,input().split())
    x = [list(map(int,input().split())) for _ in range(n)]
    ans = [0]*8
    ans[0] = sum(sorted([i+j+k for i,j,k in x],reverse=True)[:m])
    ans[1] = sum(sorted([i+j-k for i,j,k in x],reverse=True)[:m])
    ans[2] = sum(sorted([i-j+k for i,j,k in x],reverse=True)[:m])
    ans[3] = sum(sorted([i-j-k for i,j,k in x],reverse=True)[:m])
    ans[4] = sum(sorted([-i+j+k for i,j,k in x],reverse=True)[:m])
    ans[5] = sum(sorted([-i+j-k for i,j,k in x],reverse=True)[:m])
    ans[6] = sum(sorted([-i-j+k for i,j,k in x],reverse=True)[:m])
    ans[7] = sum(sorted([-i-j-k for i,j,k in x],reverse=True)[:m])
    print(max(ans))
    
if __name__ == '__main__':
    main()