def main():
    N, K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    ans = sum(a[:K])
    print(ans)
    return
main()