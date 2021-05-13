inp=input().split()
inp=[int(i) for i in inp]
N=inp[0]
height=inp[1]
width=inp[2]
cnt=0
for num in range(N):
    inp=input().split()
    if int(inp[0]) >= height and int(inp[1]) >= width:
        cnt+=1
print(cnt)