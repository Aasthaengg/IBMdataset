n=int(input())
a=[int(i)for i in input().split()]
d=lambda x:x/2

def devide(x,lst):
    global d
    for i in lst:
        if i%2 ==1:
            return x
    return devide(x+1,list(map(d,lst)))

print(devide(0,a))