def check(start, end):
    for i in range(start, end - 1):
        if s[i] == '#' and s[i + 1] == '#':
            return False
    return True


n, a, b, c, d = map(int, input().split())
s = input()
s = '#' + s + '#'

# a~c,b~d間で岩2連続は無理
if not check(a, c) or not check(b, d):
    print('No')
    exit()

# d<cなら飛び越え必要=b~d区間に3マス連続空きが必要
if d < c:
    for i in range(b, d + 1):
        if s[i - 1] == '.' and s[i] == '.' and s[i + 1] == '.':
            print('Yes')
            exit()
    print('No')
else:
    print('Yes')
