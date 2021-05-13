def main():
    a, b, c = map(int, input().split())
    if b - a == c - b:
        return "YES"
    return "NO" 
if __name__ == '__main__':
    print(main())