def main():
    A = [[int(i)-1 for i in input().split()] for j in range(3)]
    A.sort()
    if A[0] == A[1] or A[1] == A[2] or A[2] == A[0]:
        return print("NO")
    from collections import Counter
    c = Counter(sum(A, []))
    if [1, 1, 2, 2] == sorted(c.values()):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
