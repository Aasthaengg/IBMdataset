N=input()
M=int(N[:3])
N=int(N[1:4])
print(["No","Yes"][M%111==0 or N%111==0])