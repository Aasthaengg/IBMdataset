n = int(input())
d = sorted(map(int, input().split()))
med_idx = int(n/2)
print(d[med_idx]-d[med_idx-1])
