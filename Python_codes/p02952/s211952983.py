n = int(input())
count= 0
for i in range(1,n+1):
    if len(str(i)) == 1 or len(str(i)) == 3 or len(str(i)) == 5:
        count+=1
print(count)