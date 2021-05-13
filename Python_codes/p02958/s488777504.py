N = int(input())
p = list(map(int,input().split()))

count=0
for i in range(N):
    if p[i]!=sorted(p)[i]:
        count += 1
print("YES" if count/2<=1 else"NO")
