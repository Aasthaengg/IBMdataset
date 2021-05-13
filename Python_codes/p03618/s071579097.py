A = input()

freq = [0] * 26
freq_sum = 0

result = 1

for x in map(lambda c: ord(c) - ord('a'), A):
    result += freq_sum - freq[x]
    freq[x] += 1
    freq_sum += 1

print(result)