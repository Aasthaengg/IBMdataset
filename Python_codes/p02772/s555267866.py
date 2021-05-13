def main():

    N = int(input())
    A = list(map(int, input().split()))
    even = [v for v in A if v % 2 == 0]
    if all((v % 3 == 0) or (v % 5 == 0) for v in even):
        return "APPROVED"
    return "DENIED"

if __name__ == '__main__':
    print(main())
