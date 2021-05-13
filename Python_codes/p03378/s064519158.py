def main():
    N,M,X = map(int,input().split())
    A = list(map(int,input().split()))
    left = 0
    right = 0
    for i in range(N):
        if i == X:
            continue
        elif i < X and i in A:
            left += 1
        elif i > X and i in A:
            right += 1

    ans = min(left,right)
    return ans

print(main())
