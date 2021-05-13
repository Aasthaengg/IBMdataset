p = []
p.extend([i ** 2 for i in range(int(1000**(1/2)) + 1)])
p.extend([i ** 3 for i in range(int(1000**(1/3)) + 1)])
p.extend([i ** 5 for i in range(int(1000**(1/5)) + 1)])
p.extend([i ** 7 for i in range(int(1000**(1/7)) + 1)])
p.sort()
p.append(1000)
p.append(1001)
 
N = int(input())
 
for j in range(len(p) - 1):
  if p[j] <= N < p[j + 1]:
    print(p[j])