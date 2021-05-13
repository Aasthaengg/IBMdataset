a,b = map(int, input().split())

s1 = a + b
s2 = a - b
s3 = a * b

print(max(s1,s2,s3))