N=int(input())
dic={}
for _ in range(N):
    c,s=input().split()
    if c=="insert":
        dic[s]=True
    else:
        print("yes" if s in dic else "no")
