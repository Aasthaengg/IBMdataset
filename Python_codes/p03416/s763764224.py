a,b = input().split()
count = 0

anum = int(a)
bnum = int(b)

# a = list(a)
# b = list(b)


for i in range(anum,bnum+1):
    stra = str(i)
    if stra == stra[::-1]:        
        count += 1
        
print(count)
