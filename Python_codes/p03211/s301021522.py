s = input()

minDiff = abs(int(s[:3]) - 753)
for i in range(1, len(s) - 2):
    minDiff = min(minDiff, abs(int(s[i:i+3]) - 753))

print(minDiff)