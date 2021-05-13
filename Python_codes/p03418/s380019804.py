n,k = map(int,input().split())

def main():
    ans = 0
    if k!= 0:
        for b in range(k+1,n+1):
            for q in range((n-k)//b+1):
                ans += min(b-k,n-b*q-k+1)
        print(ans)
        return
    else:
        print(n*n)
        return

if __name__ == "__main__":
    main()