l = [int(input()) for _ in range(5)]

m = 9 - min([(i-1) % 10 for i in l])

print(sum([((i-1)//10 + 1) * 10 for i in l]) - m)