def func():
    cnt = 0
    def m(n):
        nonlocal cnt

        if n < 3:
            return cnt
        if n != 0:
            cnt += 1

        m(n-3)
        return cnt
    return m

n=int(input())

f=func()
print(f(n))
