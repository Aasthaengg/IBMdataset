def actual(A, B):
    is_palindrome = lambda i: str(i) == str(i)[::-1]

    return sum([is_palindrome(num) for num in range(A, B + 1)])

A, B = map(int, input().split())
print(actual(A, B))