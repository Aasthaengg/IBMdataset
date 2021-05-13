n = int(input())
text = input()

dataset = text.split()
reverse = []

for x in range(n):
    reverse.append(dataset[n-x-1])

print(' '.join(reverse))