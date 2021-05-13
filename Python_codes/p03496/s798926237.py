def main():
    _ = int(input())
    a = list(map(int, input().split()))
    ans = []
    max_a = max(a)
    min_a = min(a)
    unify_plus = True
    if max_a + min_a < 0:
        unify_plus = False
    if unify_plus:
        index = -1
        for i in range(len(a)):
            if max_a == a[i]:
                index = i
                break
        for i in range(len(a)):
            if a[i] < 0:
                a[i] += a[index]
                ans.append([index+1, i+1])
        for i in range(1, len(a)):
            if a[i-1] > a[i]:
                a[i] += a[i-1]
                ans.append([i-1+1, i+1])
    else:
        index = -1
        for i in range(len(a)):
            if min_a == a[i]:
                index = i
                break
        for i in range(len(a)):
            if a[i] > 0:
                a[i] += a[index]
                ans.append([index+1, i+1])
        for i in reversed(range(1, len(a))):
            if a[i-1] > a[i]:
                a[i-1] += a[i]
                ans.append([i+1, i-1+1])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

if __name__ == "__main__":
    main()