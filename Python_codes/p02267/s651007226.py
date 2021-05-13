n, s, q, t = input(), set(map(int, input().split())), input(), set(map(int, input().split()))
print(sum(i in s for i in t))