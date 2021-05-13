def main():
    A, B = map(int, input().split())
    if A % 3 == 0 or B % 3 == 0 or (A+B) % 3 == 0:
        return "Possible"
    return "Impossible"

if __name__ == '__main__':
    print(main())