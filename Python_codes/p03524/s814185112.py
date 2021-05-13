import collections

def main():
    S = list(input())
    Scount = collections.Counter(S)
    a = Scount['a']; b = Scount['b']; c = Scount['c']
    if abs(a-b) <= 1 and abs(b-c) <= 1 and abs(c-a) <= 1:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
