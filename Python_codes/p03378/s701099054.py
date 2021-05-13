n, m, x = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0
for i in range(x):
    if i in A:
        start += 1

for i in range(x,n+1):
    if i in A:
        end += 1

print(min(start, end))