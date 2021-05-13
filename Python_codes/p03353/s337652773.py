import re

def main():
    s = input()
    k = int(input())
    n = len(s)
    a = set()
    for i in range(n):
        for j in range(i + 1, min(n + 1, i + 1 + k)):
            a.add(s[i:j])
    print(sorted(list(a))[k - 1])

if __name__ == '__main__':
    main()