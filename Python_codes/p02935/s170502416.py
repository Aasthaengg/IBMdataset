N = int(input())
v = list(map(int, input().split()))
v.sort(reverse=True)
for i in range(N-1):
    a = v.pop()
    b = v.pop()
    v.append((a + b)/2)
print(v[0])