def main():
    N = int(input())
    A = list(map(int,input().split()))
    # 左から貪欲に1,2,3..ととっていけば良い
    next = 1
    for a in A:
        if a==next:
            next += 1
    if next==1:
        print(-1)
    else:
        print(N-(next-1))

main()
