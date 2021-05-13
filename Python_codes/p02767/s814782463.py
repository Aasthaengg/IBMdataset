n = int(input())
x = list(map(int, input().split()))
y = round(sum(x)/n)

print(sum([abs(i-y)**2 for i in x]))