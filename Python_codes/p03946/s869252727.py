def main():
    n,t = map(int,input().split())
    a = [int(x) for x in input().split()]
    a_min = []
    ap = a_min.append
    ap(a[0])
    for i in range(1,n):
        ap(min(a_min[-1],a[i]))
    a_sub = []
    ap = a_sub.append
    for i in range(n):
        ap(a[i]-a_min[i])
    print(a_sub.count(max(a_sub)))
if __name__ == "__main__":
    main()