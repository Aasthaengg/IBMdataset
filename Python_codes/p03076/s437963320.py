Time = [int(input()) for X in range(0,5)]
Loss = [(10-X%10)%10 for X in Time]
print(sum(Time)+sum(sorted(Loss)[:4]))