n = int(input())
s = input()
n_r = s.count('R')
n_b = s.count('B')
if n_r > n_b:
    print("Yes")
else:
    print("No")