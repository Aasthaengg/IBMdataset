n= int(input())
p = list(map(int, input().split()))
res = 0
for i in range(n):
    if p[i]!=i+1:res +=1
print("YES" if res <=2 else "NO")