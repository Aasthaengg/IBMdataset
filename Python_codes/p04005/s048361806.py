l = list(map(int,input().split()))

for i in l:
    if i%2==0:
        print(0)
        exit()

print(min(l[0]*l[1], l[1]*l[2], l[2]*l[0]))