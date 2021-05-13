n = int(input())
d = {"M": 0, "A": 0,"R": 0,"C": 0,"H": 0}

for i in range(n):
  s = input()
  d[s[0]] = d.get(s[0], 0) + 1

x = 0
x += d["M"] * d["A"] * d["R"]
x += d["M"] * d["A"] * d["C"]
x += d["M"] * d["A"] * d["H"]
x += d["M"] * d["R"] * d["C"]
x += d["M"] * d["R"] * d["H"]
x += d["M"] * d["C"] * d["H"]
x += d["A"] * d["R"] * d["C"]
x += d["A"] * d["R"] * d["H"]
x += d["A"] * d["C"] * d["H"]
x += d["R"] * d["C"] * d["H"]
print(x)