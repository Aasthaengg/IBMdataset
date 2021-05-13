n, m = map(int, input().split())
point = 0 ; penalty = 0
false = [0] * n
correct = [0] * n
for i in range(m) :
    p, s = input().split()
    p = int(p)
    if s == "WA" and correct[p-1] != 1 :
        false[p-1] += 1
    if s == "AC" :
        correct[p-1] = 1

for i in range(n) :
    if false[i] > 0 and correct[i] == 1 :
        penalty += false[i]

print(sum(correct),penalty)
