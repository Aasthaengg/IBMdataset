import sys
numbers = []

for i in range(3):
    for number in list(map(int, input().split())):
        numbers.append(number)

hits = []
N = int(input())
for _ in range(N):
    hits.append(int(input()))

lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

for line in lines:
    a, b, c = line
    if numbers[a] in hits and numbers[b] in hits and numbers[c] in hits:
        print('Yes')
        sys.exit()
        
print('No')