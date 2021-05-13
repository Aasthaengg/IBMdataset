def main():
    N, X = map(int, input().split())
    l = list(map(int, input().split()))
    p = 0
    record = [0]
    for i in range(N):
        p += l[i]
        if p > X:
            break
        record.append(p)
    print(len(record))
main()  