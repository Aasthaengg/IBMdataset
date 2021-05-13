n=int(input())
a=sorted(int(v)-i for i,v in enumerate(input().split()))
print(sum(abs(i-a[n//2]) for i in a))