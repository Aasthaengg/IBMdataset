def main():
    N, K = map(int, input().split())
    S = [int(a) for a in input().split()]
    S.sort(reverse = True)
    print(sum(S[:K]))
main()