n = int(input())
s,t =  input().split()
for (ele,mele) in zip(s,t):
    print(ele+mele,end="")