N = int(input())
A = list(map(int, input().split()))

lis = [0]*(N+1)
for a in A:
    lis[a] += 1
for num in lis[1:]:
    print(num)