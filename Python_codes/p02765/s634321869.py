N, R = (int(x) for x in input().split())

print(R if N >= 10 else R + 100*(10 - N))