n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
ans = a[1: 1+2*n:2]
#print(ans)
print(sum(ans))