S = input()
T = input()
Count = 0
for SC,TC in zip(S,T):
    if SC == TC:
        Count += 1
print(Count)