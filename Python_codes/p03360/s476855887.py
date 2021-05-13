def main():
    A, B, C = map(int, input().split())
    K = int(input())

    l = [A, B, C]
    l.sort(reverse=True)
    for i in range(K):
        l[0] = l[0] * 2
    print(sum(l))
main()