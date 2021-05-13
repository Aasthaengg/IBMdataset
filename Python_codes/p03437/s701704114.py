def main():

    X, Y = map(int, input().split())
    if X % Y == 0: return -1
    return X*(Y-1)

if __name__ == '__main__':
    print(main())