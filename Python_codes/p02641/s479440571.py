x,n = map(int,input().split())
p = set(map(int,input().split()))

differ = 0

while x+differ in p and x-differ in p:
    differ+=1

print(int(x-differ if x-differ not in p else x+differ))