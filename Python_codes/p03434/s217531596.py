n = int(input())
a = list(map(int, input().split()))

ali = 0
bob = 0

a.sort()
# print(a)
while True:
    if(len(a) > 0):
        ali += a.pop()
    else:
        break
    if(len(a) > 0):
        bob += a.pop()
    else:
        break

print(ali - bob)
