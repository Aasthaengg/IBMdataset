n=int(input())
arr=[int(i) for i in input().strip().split(" ")]
arr=sorted(arr)
arr=arr[::-1]
# newArr=[arr[0]]
ans=0
# for i in range(1,n//2):
#     newArr.append(arr[i])
#     newArr.append(arr[i])
for i in range(1,n):
    # print()
    ans+=arr[i//2]
print(ans)




