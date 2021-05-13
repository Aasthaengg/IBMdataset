h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

result = []
for i in range(n):
    result.extend([i+1 for _ in range(a[i])])
for i in range(h):
    out_put = result[w*i:w*(i+1)]
    if i%2==0:
        print(" ".join(list(map(str, out_put))))
    else:
        print(" ".join(list(map(str, out_put[::-1]))))