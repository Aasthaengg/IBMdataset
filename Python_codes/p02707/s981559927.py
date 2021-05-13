n = int(input())
a = [int(x) for x in input().split()]

num = [0]*(n+1)

for i in a:
    num[i] += 1

for j in range(1,n+1):
    print(num[j])
