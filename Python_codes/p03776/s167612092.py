n, a, b = map(int, input().split())
v = list(map(int, input().split()))

def combination(n, k):
    a = 1
    for i in range(k):
        a *= (n - i)
        a //= (i + 1)
    return a

v.sort(reverse = True)
average = sum(v[:a]) / a
print(average)
amount = [a]
for i in range(a + 1, b + 1):
    average2 = sum(v[:i]) / i
    if average == average2:
        amount.append(i)
    else:
        break
com = 0
for i in amount:
    v1 = v[:i]
    v2 = v[i:]
    min_v = min(v1)
    m1 = v1.count(min_v)
    m2 = v2.count(min_v)
    com += combination(m1 + m2, min(m1, m2))
print(com)