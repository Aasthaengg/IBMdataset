def main():
    N = int(input())
    A = sorted([int(_) for _ in input().split()])
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = A[i]+B[i]
    output = 1
    for i in range(N-1)[::-1]:
        if 2*B[i+1] >= A[i+1]:
            output += 1
            continue
        else: break
    print(output)
    return

if __name__ == '__main__':
    main()
