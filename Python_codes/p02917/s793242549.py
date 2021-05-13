n = int(input())
b = list(map(int, input().split()))

ans = [b[0]]

for i in range(n-2):
    ans.append(min(b[i],b[i+1]))
ans.append(b[n-2])

print(sum(ans))