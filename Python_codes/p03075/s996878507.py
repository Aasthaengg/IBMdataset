a = [int(input()) for _ in range(5)]
k = int(input())
m = min(a)
M = max(a)
if M-m <= k:
    print("Yay!")
else:
    print(":(")