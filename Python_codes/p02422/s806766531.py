N=input()
Z=int(input())
for i in range(Z):
    C=list(input().split())
    at=int(C[1])
    bt=int(C[2])
    if C[0]=="print":
      print(N[at:bt+1])
    elif C[0]=="replace":
      N=N[:at]+C[3]+N[bt+1:]
    else:
      re=N[at:bt+1]
      N=N[:at]+re[::-1]+N[bt+1:]
        

