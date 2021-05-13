N,X=map(int,input().split())
arr=list(map(str,input()))

arr[X-1]=arr[X-1].lower()


print("".join(arr))