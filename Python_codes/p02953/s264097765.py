def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    H[0] -= 1
    for i in range(1, N - 1):
        if H[i-1] < H[i]:
            H[i] -= 1
        if H[i] > H[i+1]:
            print('No')
            break
    else:
        print('Yes')
    return

main()