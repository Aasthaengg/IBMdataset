n = int(input())
li = list(map(int,input().split()))
count = 0
#print(li)
for i,l in enumerate(li):
    #print(i,l-1,li[l-1])
    if li[l-1] == i+1:
        count+= 1
print(count//2)