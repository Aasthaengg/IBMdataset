
def main():
    n = int(input())
    l = list(map(int, input().split()))
    max_l = l.pop(l.index(max(l)))
    if max_l < sum(l):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
