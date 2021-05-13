n = int(input())
x_list = list(map(int, input().split()))
m = int(sum(x_list)/n + 0.5)
print(sum((x - m)**2 for x in x_list))