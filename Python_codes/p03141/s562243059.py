n = int(input())
ab = []
for _ in range(n):
    a_, b_ = map(int, input().split())
    d = a_ + b_
    ab.append([a_, b_, d])
ab = sorted(ab, key=lambda x:x[2])[::-1]
print(sum([a[0] for a in ab[0::2]]) - sum([b[1] for b in ab[1::2]]))