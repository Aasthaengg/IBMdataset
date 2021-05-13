def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    last = p[-1]
    print(sum(p)-last+(last//2))
main()  