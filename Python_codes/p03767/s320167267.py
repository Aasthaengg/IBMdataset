n=int(input())
a=list(map(lambda x: int(x), input().split()))
a.sort(reverse=True)
print(sum(a[1:2*n:2]))