cases  = [int(i) for i in input().split() if i.isdigit()]
w = input()
print(w[0:cases[1]-1] + w[cases[1]-1].lower() + w[cases[1]:])