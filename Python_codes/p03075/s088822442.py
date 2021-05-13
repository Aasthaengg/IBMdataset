antena = [int(input()) for _ in range(5)]

k = int(input())

max_dist = max(antena)
min_dist = min(antena)

l = max_dist - min_dist

if l <= k:
    print("Yay!")
else:
    print(":(")

