a, b, c, k = list(map(int, input().split()))

num_one_cards = min(a, k)
num_zero_cards = min(b, k - num_one_cards)
num_minus_one_cards = k - num_one_cards - num_zero_cards

score = 1 * num_one_cards + 0 * num_zero_cards + (-1) * num_minus_one_cards

print(score)
