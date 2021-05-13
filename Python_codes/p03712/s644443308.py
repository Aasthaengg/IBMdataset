H,W=map(int,input().split())
A=["#"*(W+2)]+["#"+input()+"#" for i in range(H)]+["#"*(W+2)]
for a in A:
    print(*a,sep="")