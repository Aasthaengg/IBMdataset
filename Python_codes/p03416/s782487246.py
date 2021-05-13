def main():
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):
        s = str(i)
        t = list(s)
        t.reverse()
        if s == ''.join(t):
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()
