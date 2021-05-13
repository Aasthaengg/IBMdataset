tms=int(input())
strlist=sorted(list(map(int,input().split())))
ans=sum(strlist[tms::][::2])
print(ans)