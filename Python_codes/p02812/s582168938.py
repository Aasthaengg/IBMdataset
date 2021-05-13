n = int(input())
s = input()
k = 0
liss = list(s)
for i in range(len(s) - 2):
    if (liss[i] == 'A') & (liss[i + 1] == 'B') & (liss[i + 2] == 'C'):
        k += 1
print(k)