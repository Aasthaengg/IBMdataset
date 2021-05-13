def is_palindrome(s: str) -> bool:
    return s[:len(s) // 2] == s[-1 * (len(s) // 2):][::-1]

N = input()
print('Yes' if is_palindrome(N) else 'No')