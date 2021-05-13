def main():
    n = int(input())
    v = list(map(int, input().split()))
    v_s = sorted(v)

    w = v_s[0]
    for i in range(1, n):
        w = (w + v_s[i])/2
    print(w)
    
if __name__ == '__main__':
    main()