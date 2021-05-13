N=int(input())
a=list(map(int,input().split()))
t=int(len(a)-(len(a)/3))
a.sort(reverse=True)
a_cutlist=a[:t+1]
a_cutlist_ans=a_cutlist[1::2]
print(sum(a_cutlist_ans))