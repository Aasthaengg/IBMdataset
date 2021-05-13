N, K = map(int, input().split())
a = tuple(map(int, input().split()))

def main():
    l = [False] * (K+1)
    for i in range(a[0] -1, K+1):
        l[i] = any(not l[i-j] if i >= j else False for j in a)
    if l[-1]:
        print('First')
    else:
        print('Second')


main()
