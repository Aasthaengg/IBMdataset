import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    o = input()
    e = input()
    ans = []
    for i in range(max(len(o), len(e))):
        if i < len(o):
            ans.append(o[i])
        if i < len(e):
            ans.append(e[i])
    print(''.join(ans))

if __name__ == '__main__':
    main()
