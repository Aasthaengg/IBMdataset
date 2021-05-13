r = int(input())

rate = [1200, 2800, 4209]
contest = ['ABC', 'ARC', 'AGC']

for i in range(3):
    if r < rate[i]:
        break
print(contest[i])