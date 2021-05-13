n = int(raw_input())
a = map(int,raw_input().split())
s = 0
for i in range(n):
    s += a[i]
print min(a),max(a),s