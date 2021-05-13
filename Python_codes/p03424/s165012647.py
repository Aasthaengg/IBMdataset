n = int(input())
line = list(input().split())
print("Four") if len(set(line)) == 4 else print("Three")