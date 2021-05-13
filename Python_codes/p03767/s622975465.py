num = int(input())
a = sorted(list(map(int, input().split())))
print(sum(a[-2:-2 * num - 1:-2]))