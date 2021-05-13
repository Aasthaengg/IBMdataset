def main():
    X, t = map(int, input().split())
    if t <= X:
        return X-t
    return 0



if __name__ == '__main__':
    print(main())