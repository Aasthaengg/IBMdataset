n, k = [int(e) for e in input().split()]
sticks_length = list(map(int, input().split()))
sticks_length.sort(reverse=True)
print(sum(sticks_length[:k:1]))