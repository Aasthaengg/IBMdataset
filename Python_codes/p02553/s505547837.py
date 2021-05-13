a, b, c, d = map(int, input().split())

ac = a * c
ad = a * d
bc = b * c
bd = b * d

result_a = ac if ac > ad else ad
result_b = bc if bc > bd else bd

print(result_a if result_a > result_b else result_b)