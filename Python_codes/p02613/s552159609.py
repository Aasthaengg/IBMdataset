N=int(input())

C0, C1, C2, C3=0, 0, 0, 0
for i in range(N):
    s=input()
    if s=="AC":
        C0+=1
    elif s=="WA":
        C1+=1
    elif s=="TLE":
        C2+=1
    elif s=="RE":
        C3+=1
        
print("AC x "+str(C0))
print("WA x "+str(C1))
print("TLE x "+str(C2))
print("RE x "+str(C3))