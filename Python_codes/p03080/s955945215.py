# Your code here!
def pin(type=int):
    return map(type,input().split())


N, =(pin())
s, =pin(str)

counter =0
for i in range(N):
    if s[i] == "R":
        counter +=1
        
if (counter > N-counter):
    print("Yes")
else:
    print("No")