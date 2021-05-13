n,a,b,c,d=map(int,input().split())
a-=1
b-=1
c-=1
d-=1

s=input()

if c<d or c<b:
    #先にbをdに運んでから、aをCに運べばいい
    if s[b:d+1].count("##")==0 and s[a:c+1].count("##")==0:
        print("Yes")
    else:
        print("No") 
else:
    if s[b-1:d+2].count("...")==0:
        print("No")
    else:
        if s[b:d+1].count("##")==0 and s[a:c+1].count("##")==0:
            print("Yes")
        else:
            print("No") 




