n = int(input())
ab_array = sorted([[int(x) for x in input().split()] for y in range(n)], key=lambda x: x[0])
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
print(ab_array[-1][0] + ab_array[-1][1])