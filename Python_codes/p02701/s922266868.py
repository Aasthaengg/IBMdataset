n=int(input())
lst=set([])
counter=0
for _ in range(n):
    s=input()
    if s in lst : continue
    lst.add(s)
    counter+=1

print(counter)