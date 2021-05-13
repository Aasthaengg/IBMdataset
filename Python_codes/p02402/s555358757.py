
n=int(input())
list=list(map(int,input().split()))
list.sort()
print(str(list[0])+" "+str(list[n-1])+" "+str(sum(list)))