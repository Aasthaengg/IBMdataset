n, a, b, c, d = map(int, input().split())
s = '_' + input()

if s[c] == '#' or s[d] == '#':
    print('No')
    exit()

# '##'を検知
if '##' in s[a:c+1] or '##' in s[b:d+1]:
    print('No')
    exit()

if c > d:
    # 3 マス以上の連続する'.'が必要
    num_dot = s[b-1:d+2].count("...")
    if num_dot == 0:
        print('No')
        exit()

print('Yes')