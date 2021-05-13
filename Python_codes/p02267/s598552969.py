n=int(input())
S=input().split(" ")
q=int(input())
T=input().split(" ")

count=0
for t in T:
    for s in S:
        if t==s:
            count+=1
            break

print(count)

