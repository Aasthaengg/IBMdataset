def main(s):
    code = ord(s)
    if ord('a') <= code <= ord('z'):
        return 'a'
    if ord('A') <= code <= ord('Z'):
        return 'A'

if __name__ == '__main__':
    s = input()
    ans = main(s)
    print(ans)

