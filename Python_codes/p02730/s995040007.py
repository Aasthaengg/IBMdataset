import sys


def is_palindrome(s):
    if len(s) % 2:
        a, b = s[:len(s) // 2], s[len(s) // 2 + 1:]
    else:
        a, b = s[:len(s) // 2], s[len(s) // 2:]
    return a == ''.join(reversed(b))


def resolve(in_):
    s = in_.readline().strip()
    ret = is_palindrome(s) and is_palindrome(s[:len(s) // 2]) and is_palindrome(s[len(s) // 2 + 1:])
    return 'Yes' if ret else 'No'


def main():
    answer = resolve(sys.stdin)
    print(answer)


if __name__ == '__main__':
    main()
