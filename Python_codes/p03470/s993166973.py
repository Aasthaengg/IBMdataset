s = input()
n = int(s)

mochies = []

for i in range(n):
    p = input()
    q = int(p)
    mochies.append(q)

mochies.sort()

count = 1

for i in range(len(mochies)):
    if i + 1 == len(mochies):
        break
    if mochies[i] < mochies[i + 1]:
        count += 1
    else:
        continue
    
print(count)
