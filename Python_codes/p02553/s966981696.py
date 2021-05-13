a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

temp1 = a*c
temp2 = a*d
temp3 = b*c
temp4 = b*d

answer = max(temp1,temp2,temp3,temp4)

print(answer)