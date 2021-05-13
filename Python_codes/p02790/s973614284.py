# https://atcoder.jp/contests/abc152/tasks/abc152_b

a, b = map(int, input().split())
s1 = ("{}".format(a)) * b
s2 = ("{}".format(b)) * a

if s1 <= s2:
    print(s1)
else:
    print(s2)