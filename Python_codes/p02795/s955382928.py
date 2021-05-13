H=int(input())
W=int(input())
N=int(input())
cnt=0
M=0
if H>W:
    selection=H
else:
    selection=W
while M<N:
    cnt+=1
    M+=selection

print(cnt)

