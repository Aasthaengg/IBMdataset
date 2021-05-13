n=int(input())
answer=[]
d={}
for i in range(n):
    cmd,word=input().split()
    if cmd=="insert":
        d[word]=True
    
    else:
        if word in d:
            print("yes")

        else:
            print("no")


