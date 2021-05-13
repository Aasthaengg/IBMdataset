line = input()
A,B,C = [int(n) for n in line.split()]
print(min(B//A,C))