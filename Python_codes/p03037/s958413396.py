data=input().split()
N=int(data[0])
M=int(data[1])
data_gate=[input().split() for i in range(M)]
data_min=[]
data_max=[]
for i in range(M):
    data_min.append(int(data_gate[i][0]))
    data_max.append(int(data_gate[i][1]))
m=max(data_min)
M=min(data_max)
if M>=m:
    ans=M-m+1
else:
    ans=0
print(ans)