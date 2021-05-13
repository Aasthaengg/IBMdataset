def main():
    a, b = map(int, input().split())
    if a <= b: return a
    else: return a-1

if __name__ == '__main__':
    print(main())