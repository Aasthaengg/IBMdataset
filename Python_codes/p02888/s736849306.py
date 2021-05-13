N = int(input())
L = list(map(int,input().split()))

L.sort(reverse=True)
counter = 0
import bisect

for index1,c in enumerate(L):
    for index2,b in enumerate(L[index1+1:],start=index1+1):
        left = 0 ; right = N
        oppai = c-b
        while left+1<right:
            mid = (left+right)//2
            if L[mid]>oppai:
                left = mid
            else :
                right=mid
        
        index3 = left
        
        if index3>index2:

            counter += index3-index2
print(counter)