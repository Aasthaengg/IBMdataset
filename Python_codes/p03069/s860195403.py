n = int(input())
s = input()
rw = s.count(".")
lb = 0
M = rw+lb
for i in range(n):
    if s[i] =="#":
        lb += 1
    else:
        rw -= 1
    M = min(M,rw+lb)
print(M)