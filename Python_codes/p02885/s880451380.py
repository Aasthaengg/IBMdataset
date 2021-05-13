def q1():
    A,B = (int(i) for i in input().split())
    ans = max(0, A - B*2)
    print(ans)


if __name__ == '__main__':
    q1()
