#n=int(input())
#n,m=map(int,input().split())
#al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
s=list(input())

count1=s.count("1")
count0=s.count("0")

print(min(count1,count0)*2)
