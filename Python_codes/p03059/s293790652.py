def q1():
    A, B, T = (int(i) for i in input().split())
    d,_ = divmod(T, A)
    ans = B * d
    return ans

if __name__ == '__main__':
    print(q1())