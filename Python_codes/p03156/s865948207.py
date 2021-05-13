n = int(input())
a, b = map(int, input().split())
p = [int(x) for x in input().split()]


q1 = sum(x <= a for x in p)
q2 = sum(a < x <= b for x in p)
q3 = sum(b < x for x in p)

print(min(q1, q2, q3))

