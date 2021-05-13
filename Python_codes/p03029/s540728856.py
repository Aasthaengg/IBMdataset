def q1():
    A,P = (int(i) for i in input().split())
    sum = A * 3 + P
    ans,_ = divmod(sum, 2)
    print(ans)


if __name__ == '__main__':
    q1()