n = int(input())
ans = [0]*n
for i in range(n):
    a, b = map(str, input().split())
    b = int(b)
    ans[i] = [i+1, a, b]
ans.sort(key=lambda x: (x[1], -x[2]))
for j in ans:
    print(j[0])