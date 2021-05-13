h = int(input())
w = int(input())
n = int(input())

if w > h:
    h, w = w, h

print((n+h-1)//h)
