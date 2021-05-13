def main():
    K, X = map(int, input().split())
    if K == 1:
        print(X)
        return
    ans = []
    ans.append(X)
    l = X
    r = X
    for i in range(K - 1):
        l = l - 1
        r = r + 1
        ans.append(l)
        ans.append(r)
    ans.sort()
    a = ''
    for i in range(len(ans)):
        a = a + str(ans[i]) + ' '
    print(a)
main()  