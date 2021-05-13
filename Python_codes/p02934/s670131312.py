import statistics
n = int(input())
print(statistics.harmonic_mean(map(int, input().split())) / n)