# https://atcoder.jp/contests/abc087/tasks/abc087_b

A = int(input())
B = int(input())
C = int(input())
X = int(input())

possible_values = [a * 500 + b * 100 + c * 50 for a in range(A+1) for b in range(B+1) for c in range(C+1)]
is_match = [1 for i in possible_values if i == X]
print(sum(is_match))