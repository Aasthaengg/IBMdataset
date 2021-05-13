a=list(map(int,input().split()))
k=int(input())
for i in range(k):
    a=sorted(a)
    a[-1]*=2
print(sum(a))