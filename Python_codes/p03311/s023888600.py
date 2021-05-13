n = int(input())

a = list(map(int,input().split()))

b = []

for i in range(n):
    b.append(a[i]-i)
    
b.sort()

kb = [b[n//2],b[n//2]]

ans = []

for i in kb:
    x = 0
    for s in range(len(a)):
        x += abs(a[s]-i-s)
    ans.append(x)
    
print(min(ans))