A,B,C = map(int,input().split())
temp = A - B
remain = C - temp

if remain < 0:
    remain = 0
    
print(remain)