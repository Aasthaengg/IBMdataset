n = int(input())
l = [int(i) for i in input().split()]

dummy = -9999
prev = dummy
ct = 0
for i in l:
    if i == prev:
        ct += 1
        prev = dummy
    else:
        prev = i
        
print(ct)