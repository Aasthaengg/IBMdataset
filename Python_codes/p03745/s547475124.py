def main():
    N = int(input())
    lst = [int(_) for _ in input().split()]
    last = lst[0]
    A = [last]
    for i in range(1, N):
        if lst[i] == last: continue
        last = lst[i]
        A.append(lst[i])
    left = right = output = 0
    while left < len(A):
        if left == len(A)-1:
            output += 1
            break
        if A[left+1] - A[left] > 0:
            while right < len(A)-1 and A[right] < A[right+1]:
                right += 1
        elif A[left+1] - A[left] < 0:
            while right < len(A)-1 and A[right] > A[right+1]:
                right += 1
        output += 1
        left = right + 1
        right = left
    print(output)
    return

if __name__ == '__main__':
    main()
