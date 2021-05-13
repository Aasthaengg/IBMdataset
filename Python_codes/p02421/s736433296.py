n = int(raw_input())
a = b = 0
for i in range(n):
    tmp = raw_input().split()
    if tmp[0] > tmp[1]:
        a+=3
    elif tmp[0] < tmp[1]:
        b+=3
    else:
        a+=1
        b+=1
print a, b
