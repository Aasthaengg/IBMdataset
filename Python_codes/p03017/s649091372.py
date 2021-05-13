n,a,b,c,d=map(int,input().split())
s=str(input())

if c<d:
    if s[min(a,b)-1:d+1].count("##")==0:
        print("Yes")
    else:
        print("No")
else:
    if s[min(a,b)-1:d+1].count("##")==0:
        if s[max(a,b)-2:d+1].count("...")==0:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
