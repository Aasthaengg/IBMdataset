n = int(input())

d = [0]* 101
for i in range(n+1):
    i0 = i + 0
    for j in range(2, i0+1):
        while i % j == 0:
            d[j] += 1
            i = i //j

d.sort()
d1 = [i for i in d if i >=2]

def num(m): # e の要素のうち m-1 以上のものの個数
    return len(list(filter(lambda x: x >= m-1, d1)))

print(num(75) + num(25) * (num(3) - 1) + num(15) * (num(5) - 1) + num(5) * (num(5) - 1) * (num(3) - 2) // 2)
