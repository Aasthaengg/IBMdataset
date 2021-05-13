n = int(input())
la = [int(w) for w in input().split()]

odd_pat = 1
max_pat = 3**n

for a in la:
    if a % 2 == 0:
        odd_pat *= 2


print(max_pat-odd_pat)
