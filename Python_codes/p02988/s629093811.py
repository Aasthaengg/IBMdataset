N=int(input())
arr=list(map(int,input().split()))
count=0

for i in range(N-2):
    if arr[i+1]!=max(arr[i:i+3]) and arr[i+1]!=min(arr[i:i+3]):
        count+=1

print(count)