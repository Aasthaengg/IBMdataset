n = int(input().rstrip())
l = input().rstrip().split()
result = ''
for i in range(n):
    result += l[0][i] + l[1][i]

print(result)
