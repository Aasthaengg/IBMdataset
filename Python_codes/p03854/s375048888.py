# C - 白昼夢
def main():
    s = list(input())
    
    while len(s) != 0:
        if ''.join(s[-5:]) == 'dream':
            for _ in range(5):
                s.pop()
        elif ''.join(s[-7:]) == 'dreamer':
            for _ in range(7):
                s.pop()
        elif ''.join(s[-5:]) == 'erase':
            for _ in range(5):
                s.pop()
        elif ''.join(s[-6:]) == 'eraser':
            for _ in range(6):
                s.pop()
        else:
            print('NO')
            exit()
    else:
        print('YES')


if __name__ ==  "__main__":
    main()