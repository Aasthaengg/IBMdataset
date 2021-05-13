h,w,a,b = map(int, input().split())

s='0'*a
s+='1'*(w-a)
for i in range(b):
    print(s)
s='1'*a
s+='0'*(w-a)
for i in range(h-b):
    print(s)
