n, k = map(int, input().split())
s = input()

part1 = s[:k - 1]
part2 = s[k - 1].lower()
part3 = s[k:]

# print(f'{part1}{part2}{part3}')
print('{part1}{part2}{part3}'.format(part1=part1, part2=part2, part3=part3))
