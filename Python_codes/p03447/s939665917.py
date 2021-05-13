X = int(input())
A = int(input())
B = int(input())

buf = X - A
while True:
    if buf - B < 0:
        break
    buf -= B
print(buf) 
