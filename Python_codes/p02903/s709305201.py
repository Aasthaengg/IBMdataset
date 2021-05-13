h,w,a,b = map(int, input().split())
x = w-a
y = h-b
p = "0"*x + "1"*a
q = "1"*x + "0"*a
for i in range(b):
    print(p)
for i in range(y):
    print(q)