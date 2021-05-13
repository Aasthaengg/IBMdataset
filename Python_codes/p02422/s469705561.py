s=list(input())
q=int(input())

for i in range(q):
    cmd=list(input().split())
    
    if cmd[0]=="replace":
        s[int(cmd[1]):int(cmd[2])+1]=cmd[3]
        
    if cmd[0]=="reverse":
        ts=s[int(cmd[1]):int(cmd[2])+1]
        ts.reverse()
        s[int(cmd[1]):int(cmd[2])+1]=ts
        
    if cmd[0]=="print":
        ts=s[int(cmd[1]):int(cmd[2])+1]
        print("".join(ts))