def q1():
    A, B = (int(i) for i in input().split())

    ans = 0
    for i in range(2):
        if A > B:
            ans += A
            A -= 1
        else:
            ans += B
            B -= 1
        
    return ans


if __name__ == '__main__':
    print(q1())
