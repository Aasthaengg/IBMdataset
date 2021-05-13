from sys import stdin
h,w,b,a = map(int,stdin.readline().rstrip().split())
li = []
for i in range(a):
    s = "0"*b+"1"*(w-b)
    li.append(s)
for j in range(h-a):
    s = "1"*b+"0"*(w-b)
    li.append(s)
for i in li:
    print(i)