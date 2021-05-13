nDays = int(input())

today = [int(x) for x in input().split()]

for i in range(nDays - 1):
    tomorrow = [int(x) for x in input().split()]
    tomorrow[0] += max(today[1], today[2])
    tomorrow[1] += max(today[0], today[2])
    tomorrow[2] += max(today[0], today[1])
    today = tomorrow

print(max(today))