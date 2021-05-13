# A - Addition and Subtraction Easy
# https://atcoder.jp/contests/abc050/tasks/abc050_a

a, op, b = map(str, input().split())

result = eval(a + op + b)

print(int(result))
