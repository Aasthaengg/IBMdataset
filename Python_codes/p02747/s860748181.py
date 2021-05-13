S=input()
N=len(S)
if N%2!=0:
    print("No")
    exit()

for i in range(N//2):
    if S[i*2:(i*2)+2]!="hi":
        print("No")
        exit()
print("Yes")