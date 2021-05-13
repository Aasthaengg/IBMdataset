def main():
    N, *A = map(int, open(0).read().split())
    B = [A[i] - i - 1 for i in range(N)]
    B.sort()
    b1 = B[(N-1)//2]
    b2 = B[N//2]
    ans1 = ans2 = 0
    for i in range(N):
        a = A[i] - i - 1
        ans1 += abs(a - b1)
        ans2 += abs(a - b2)
    print(min(ans1, ans2))

if __name__ == '__main__':
  main()
