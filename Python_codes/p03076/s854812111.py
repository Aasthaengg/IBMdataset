a = []
for i in range(5):
    a.append(int(input()))
y = 0
x = [i%10 for i in a]
if max(x) > 0:
    y = 10 - min(filter(lambda i:i!= 0, x))
b = [(i+9) // 10 *10 for i in a]
print(sum(b) - y)
