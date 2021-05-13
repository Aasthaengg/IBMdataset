N = int(input())
A_ls = map(int, input().split(' '))
result = 0
for A in A_ls:
    result += 1 / A
print(1/result)