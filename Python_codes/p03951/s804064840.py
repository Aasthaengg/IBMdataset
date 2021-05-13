N=int(input())
s=input()
t=input()

for i in range(N):
    F=0
    for j in range(i,N):
        if s[j]==t[j-i]:
            continue
        else:
            F=1
            break
    if F==0:
        print(len(s[:i]+t))
        exit()
print(2*N)
