input()
LOVE = [int(i) for i in input().split(' ')]
print(int(len([1 for i in range(len(LOVE)) if i + 1 == LOVE[LOVE[i] - 1]]) / 2))