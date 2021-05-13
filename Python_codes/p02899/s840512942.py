n = int(input())
a = list(map(int,input().split()))
#(順位,出席番号)
a = [(a[i], i+1) for i in range(n)]
a.sort(key=lambda x: x[0])
b = list(zip(*a))
ans = b[1]

print(*ans)
