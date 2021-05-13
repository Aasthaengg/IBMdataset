def work(n, t, a):
    if t[-1] != a[0]:
        return 0

    middle = 0
    for i in xrange(n):
        if t[i] == a[i]:
            if t[i] != t[-1] or t[i] != a[0]:
                return 0
            middle = i
            break
    for i in xrange(middle, n):
        if t[i] < a[i]:
            return 0

    record = [None] * n
    left, right = 0, n - 1

    while left <= right and t[left] < a[left]:
        if not left or t[left] > t[left-1]:
            record[left] = 1
        else:
            record[left] = t[left]
        left += 1
    
    record[left] = 1
    while left < right and a[right] <= t[right]:
        if right == n - 1 or a[right] > a[right+1]:
            record[right] = 1
        else:
            record[right] = a[right]
        right -= 1

    ans = 1
    for i in xrange(n):
        ans = (ans*record[i]) % (10**9+7)
    return ans


n = int(raw_input())
t = map(int, raw_input().split())
a = map(int, raw_input().split())

print work(n, t, a)
