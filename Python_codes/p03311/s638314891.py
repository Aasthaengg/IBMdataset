N = int(input())
src = list(map(int,input().split()))
 
dis = [a-i-1 for i,a in enumerate(src)]
center = sorted(dis)[N//2]
 
ans = 0
for a in dis:
    ans += abs(a - center)
print(ans)