n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
bigger_a = bigger_b = 0
for a_, b_ in zip(a, b):
    if a_ > b_: bigger_a += a_ - b_
    if b_ > a_: bigger_b += (b_ - a_) // 2
if bigger_b >= bigger_a: print("Yes")
else: print("No")