import sys
read = sys.stdin.read
readlines = sys.stdin.readlines

def main():
    s = tuple(input())
    t = tuple(input())
    s_len = len(s)
    t_len = len(t)
    r = s_len
    for i1 in range(s_len - t_len + 1):
        s2 = s[i1:i1 + t_len + 1]
        tmp0 = sum([se != te for se, te in zip(s2, t)])
        r = min(r, tmp0)
    print(r)

if __name__ == '__main__':
    main()
