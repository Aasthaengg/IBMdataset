N=int(input())
A=list(map(int,input().split()))
i=0
for a in A:
    if a%2==0:
        if a%3==0 or a%5==0:
            i=0
        else:
            print("DENIED")
            i=1
            break

if i==0:
    print("APPROVED")
