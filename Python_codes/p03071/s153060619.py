
if __name__ == "__main__":
    A, B = [int(a) for a in input().split()]
    cnt = 0
    for i in range(2):
        if A >= B:
            cnt += A
            A -= 1
        else:
            cnt += B
            B -= 1
    print(cnt)
