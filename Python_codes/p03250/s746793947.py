import statistics

l = list(map(int, input().split()))

print(int(str(max(l))+str(min(l))) +statistics.median(l))