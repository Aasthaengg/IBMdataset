n = input()
nt = sum(map(int, n))
a = (len(n)-1)*9 + int(n[0])-1
print(nt if a < nt else a)