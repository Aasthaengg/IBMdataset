n,h,w = input().split()
a = [0] * int(n)
b = [0] * int(n)
i = 0
while i < int(n):
    a[i],b[i] = input().split()
    i = i + 1

i = 0
flag = 0

while i < int(n):
    if int(a[i]) >= int(h) and int(b[i]) >= int(w):
        flag = flag + 1
    i = i + 1
print(flag)