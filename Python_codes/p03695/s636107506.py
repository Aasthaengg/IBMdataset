N = int(input())
a = list(map(int,input().split()))
b = [a[i]//400 for i in range(N) if a[i] < 3200]
c = len(set(b))
print(max(1,c), c+N-len(b))