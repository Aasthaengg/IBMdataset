h = int(input())
w = int(input())
n = int(input())
def paint(num):
    if num >= n:
        print(1)
    else:
        k = 0
        c = 0
        while k < n:
            k +=num
            c+=1
        print(c)

if h <= w:
    paint(w)
else:
    paint(h)