import statistics
import sys

data_sets = sys.stdin.read().split("\n")

for i in data_sets[1:-1:2]:
    data_set = map(int, i.split())
    print(statistics.pstdev(data_set))