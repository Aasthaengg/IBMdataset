def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
a,b = iim()
P = iil()

p1 = []
p2 = []
p3 = []

for item in P:
    if item <= a:
        p1.append(item)
    elif item <= b:
        p2.append(item)
    else:
        p3.append(item)
print(min(len(p1),len(p2),len(p3)))