import sys
S = input()
N = len(S)

def is_palindrome(s):
    return s == s[::-1]

if not is_palindrome(S):
    print('No')
    sys.exit()

if not is_palindrome(S[0:int((N - 1) / 2)]):
    print('No')
    sys.exit()

if not is_palindrome(S[int((N + 3) / 2 - 1):]):
    print('No')
    sys.exit()

print('Yes')