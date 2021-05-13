n = int(input())
num = [0] * n
employee = list(map(int,input().split()))

for i in employee:
    num[i-1] += 1

for j in num:
    print(j)
