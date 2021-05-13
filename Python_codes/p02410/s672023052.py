n,m = map(int,raw_input().split())
gyoretu = []
bekutoru = []
for i in range(n):
    gyoretu.append(map(int,raw_input().split()))
for i in range(m):
    bekutoru.append(input())

for a in gyoretu:
    i = 0
    for b in range(len(bekutoru)):
        i = i + (a[b] * bekutoru[b])
    print i