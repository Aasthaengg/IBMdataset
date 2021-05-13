n = [0] + list(map(int, input())) + [0]
n = n[::-1]
#print(n)

b0 = [0]*len(n)
b1 = [0]*len(n)
b1[0] = 1
for i in range(1, len(n)):
  num = n[i]
  b0[i] = min(b0[i-1]+num, b1[i-1]+num+1)
  b1[i] = min(b0[i-1]+10-num, b1[i-1]+10-(num+1))

print(min(b0[-1], b1[-1]))
#print(b0[-1], b1[-1])