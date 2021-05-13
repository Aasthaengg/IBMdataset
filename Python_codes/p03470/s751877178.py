def main():
    N = int(input())
    d = []
    for i in range(N):
        d.append(int(input()))
    d.sort()
    d.reverse()
    t = 101
    cnt = 0
    for i in range(len(d)):
        if t > d[i]:
            t = d[i]
            cnt += 1
    print(cnt)
main()  