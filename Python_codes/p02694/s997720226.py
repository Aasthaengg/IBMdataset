from sys import stdin
rs = stdin.readline
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    X = ri()
    money = 100
    month = 0
    while money < X:
        money += money // 100
        month += 1
    print(month)
    
if __name__ == '__main__':
    main()
