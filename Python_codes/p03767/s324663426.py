n = int(input())
a = sorted(list(map(int, input().split())))[::-1]

print(sum([a[2*i+1] for i in range(n)]))