a=list(map(int,input().split()))
k=int(input())
a.sort()
for _ in range(k):
    a[-1]*=2
print(sum(a))