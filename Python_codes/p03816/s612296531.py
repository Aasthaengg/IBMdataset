n = int(input())
a = list(map(int,input().split()))
b = [0 for i in range(100000+1)]
for i in range(n):
    b[a[i]] += 1
eat = 0
for i in range(100000+1):
    eat += max(0, b[i]-1)
print(n-(eat+1)//2*2)
