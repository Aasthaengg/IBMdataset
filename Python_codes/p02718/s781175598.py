def main():
    n,m = map(int, input().split())
    a = list(map(int,input().strip().split()))
    t = sum(a)
    c = 0
    for aa in a:
        if aa >= t / (4*m):
            c += 1
    if c >= m:
        print("Yes")
        return 
    else:
        print("No")
        return
main()
