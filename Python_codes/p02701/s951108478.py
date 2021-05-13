n = int(input())

keihin = dict()

for i in range(n):
    s = input()
    if s in keihin:
        keihin[s] += 1
    else:
        keihin[s] = 1
print(len(keihin))
