def main():
    n,m=map(int,input().split())
    a=set(int(input()) for _ in range(m))
    pattern = [0] * (n+1)
    pattern[0] = 1
    for i in range(n-1):
        if i in a:
            continue
        if i+1 not in a:
            pattern[i+1] += pattern[i]
            pattern[i+1] %= 1000000007
        if i+2 not in a:
            pattern[i+2] += pattern[i]
            pattern[i+2] %= 1000000007
    pattern[n] += pattern[n-1]
    pattern[n] %= 1000000007
    print(pattern[n])
    
if __name__ == "__main__":
    main()