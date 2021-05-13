

def main():
    n = int(input())
    d = set()
    for _ in range(n):
        op, s = input().split()
        if op == 'insert':
            d.add(s)
        else:
            if s in d:
                print('yes')
            else:
                print('no')

if __name__ == '__main__':
    main()
