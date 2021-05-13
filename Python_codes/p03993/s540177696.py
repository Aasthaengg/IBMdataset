n=int(input())
a=list(map(int,input().split()))
cnt=[i for i in range(n) if a[a[i]-1]-1==i]
print(len(cnt)//2)