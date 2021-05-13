S=input()
A=S.find("C")
print("YNeos"[not(A>=0 and S.find("F", A+1)>=0)::2])