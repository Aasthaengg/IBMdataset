# CODE FESTIVAL 2016 予選 A: B – 仲良しうさぎ / Friendly Rabbits
N = int(input()) - 1
a = [int(s) - 1 for s in input().split()]

pairs = 0

for i in range(N):
    if a[i] != 0 and a[a[i]] == i:
        pairs += 1
        a[i] = 0
        a[a[i]] = 0

print(pairs)