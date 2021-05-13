def main():

    N = int(input())
    A = list(map(int, input().split()))
    ave = sum(A)/N
    min_d = float('inf')
    min_i = None
    for i in range(N):
        d = abs(A[i]-ave)
        if d < min_d:
            min_d = d
            min_i = i
    return min_i

if __name__ == '__main__':
    print(main())