def main():

    N = int(input())
    A, B = map(int, input().split())
    P = list(map(int, input().split()))
    count = [0, 0, 0]
    for p in P:
        if p <= A:
            count[0] += 1
        elif A < p <= B:
            count[1] += 1
        else:
            count[2] += 1
    return min(count)

if __name__ == '__main__':
    print(main())