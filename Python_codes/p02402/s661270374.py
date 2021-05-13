count = int(raw_input())

arr = map(int, raw_input().split())

print("{} {} {}".format(min(arr), max(arr), sum(arr)))