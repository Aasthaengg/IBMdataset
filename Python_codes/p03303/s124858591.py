
a = input()
b = int(input())

l =[]
k = 0
s = a[0]
for i in a:
    if k == b:
        s+=i
        k =0
    k+=1
print(s)