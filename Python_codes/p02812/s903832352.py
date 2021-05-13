n = int(input())
s = input()
cs = list(s)

ss = []
for i in range(len(cs)-2):
  ss.append(cs[i]+cs[i+1]+cs[i+2])

count = 0
for i in ss:
  if i == "ABC":
    count += 1
  
print(count)
