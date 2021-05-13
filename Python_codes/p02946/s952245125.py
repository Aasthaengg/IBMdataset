k,x=map(int,input().split())
output=[]
for i in range(k-1):
    output.append(str(x-(k-1)+i))
    output.append(" ")

for i in range(k):
    output.append(str(x+i))
    output.append(" ")

output.pop()
print("".join(output))