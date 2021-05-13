n=int(input())
alist=list(map(int,input().split()))

sum=0
for a in alist:
    sum += 1 / a
print(1 / sum)