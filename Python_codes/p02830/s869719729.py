n = int(input())
s,t = input().split()
print(*[i+j for i,j in zip(s,t)],sep="")
