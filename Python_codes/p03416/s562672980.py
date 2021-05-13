def is_palindromic(n):
    s = str(n)
    for i in range(len(s)//2 + 1):
        if s[i] != s[-i-1]:
            return False
    return True

A, B = list(map(int, input().split()))
ans = 0
for n in range(A, B + 1):
    if is_palindromic(n):
        ans += 1
print(ans)