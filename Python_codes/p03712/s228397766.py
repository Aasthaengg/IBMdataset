h, w = list(map(int, input().split()))
s = []
for i in range(h):
    s.append(input())
print("#" * (w + 2))
for i in s:
    print("#%s#" % i)
print("#" * (w + 2))