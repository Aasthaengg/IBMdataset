
def main():
    K = int(input())
    cnt = 1
    a = 7%K
    s = {a}
    for i in range(K):
        if a%K == 0:
            print(cnt)
            return
        a = a*10 + 7
        a = a % K
        if a in s:
            print(-1)
            return
        s.add(a)
        cnt += 1

if __name__ == "__main__":
    main()