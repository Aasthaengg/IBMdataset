h = int(input())
w = int(input())
n = int(input())

i=1
while n > max(h,w)*i:
    i += 1
else: print(i)
