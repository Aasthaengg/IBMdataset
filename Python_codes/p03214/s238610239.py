def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    mean = sum(A)/N
    ans = []
    for i in range(N):
        ans.append(abs(A[i]-mean))
    min_ = min(ans)
    for i in range(N):
        if ans[i]==min_:
            print(i)
            exit()
if __name__ == '__main__':
    main()