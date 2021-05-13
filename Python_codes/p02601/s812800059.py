read = lambda: list(map(int, input().split()))
card = read()
k = int(input())
for _ in range(k):
    if card[0] >= card[1]:
        card[1] *= 2
    elif card[1] >= card[2]:
        card[2] *= 2

if card[0] < card[1] < card[2]:
    print("Yes")
else:
    print("No")