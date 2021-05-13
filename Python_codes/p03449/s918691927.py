n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
print(max([sum(a1[:i]+a2[i-1:]) for i in  range(1, n+1)]))