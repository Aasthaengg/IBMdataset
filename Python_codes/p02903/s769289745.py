h,w,a,b = map(int, input().split( ))

s1 = "0"*a+"1"*(w-a)
s2 = "1"*a + "0"*(w-a)
for _ in range(b):
    print(s1)
for _ in range(h-b):
    print(s2)