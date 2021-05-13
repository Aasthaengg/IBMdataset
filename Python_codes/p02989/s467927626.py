def main():
    n = int(input())
    d = list(map(int, input().split()))
    d_s = sorted(d)
    idx = int(n/2)
    diff = d_s[idx] - d_s[idx-1]
    print(diff)
    
if __name__ == '__main__':
    main()