import sys
input = sys.stdin.readline

s = input()
count0 = s.count("0")
count1 = s.count("1")

print(2 * min(count0, count1))