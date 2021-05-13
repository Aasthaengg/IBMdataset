abc=list(input())
out=[]
for x in range(0,len(abc),2):
    out.append(abc[x])
print("".join(out))