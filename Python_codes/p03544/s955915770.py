a = [2, 1]
n = int(input())
while(len(a) != n+1):
  a.append(a[-1] + a[-2])
print(a[-1])