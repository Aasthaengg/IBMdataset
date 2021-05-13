
def main():
    s = set()
    n = int(input())
    for _ in range(n):
        com = input().split()
        if com[0] == 'insert':s.add(com[1])
        else :
            if com[1] in s:print('yes')
            else          :print('no')


if __name__ == '__main__':
    main()


