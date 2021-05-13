s = input()

num = []

for i in range(len(s)-2):
  n = int(''.join(s[i:i+3]))
  num.append(abs(n-753))
  
print(min(num))