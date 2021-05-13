def main():
    N = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    total = 0
    for i in range(N-1):
        total = total + l[i]
    if total > l[N-1]:
        print('Yes')
    else:
        print('No')
main()