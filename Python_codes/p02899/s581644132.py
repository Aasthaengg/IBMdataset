N=int(input())
arr=list(map(int,input().split()))
brr=[]

for i in enumerate(arr):
    brr.append(i)
#print(brr)

brr.sort(key=lambda x:x[1])

for i in brr:
    print(i[0]+1)
