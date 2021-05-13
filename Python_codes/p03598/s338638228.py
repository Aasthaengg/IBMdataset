N = int(input())
K = int(input())
x = list(map(int,input().split()))
ans = []
for i in x:
    ans.append(min(i*2,(K-i)*2))
print(sum(ans))