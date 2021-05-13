# あえてややこしいコードにします。　いろいろ使ってみたい
bell1, bell2, bell3 = map(int, input().split())

bell_list = [bell1, bell2, bell3]
min_price_bell = []

bell_list.sort()

for i in range(0, 2):
    min_price_bell.append(bell_list[i])

print(sum(min_price_bell))
