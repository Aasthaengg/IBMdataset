# 解説見た

def solve(k, n):
    q, r = divmod(k, n)
    a = list(range(q, n + q))

    max_ = n + q - 1
    for i in range(r):
        a[i] += n
        for j in range(n):
            if i == j:
                continue
            a[j] -= 1
            if a[j] < 0:
                return []

        if a[i] < max_:
            return []
        else:
            max_ = a[i]
    return a


if __name__ == '__main__':
    k = int(input())
    for n in range(2, 50 + 1):
        a = solve(k, n)
        if all(map(lambda x: x <= 10 ** 16 + 1000, a)):
            print(n)
            print(*a)
            break

"""
2≦N≦50,0≦ai≦10**16+1000でなければならないのでダメ。

k:偶数
(x+1,x) -> (x,x-1) 操作2回
-> (1,0)
k:奇数
(x+2,x) -> (x+1,x-1) 操作2回
-> (2,0) -> (0,1)
全体を2減らすのに操作2回
k=2より最終値は0/1なので、
偶数なら(2x+1)-1=2x=k
奇数なら(2x+2)-2+1=2x+1=k
したがって、x=k//2

n = 2
x = k // 2
a = (x, x + (1 if k % 2 == 0 else 2))
print(n)
print(*a)
"""
