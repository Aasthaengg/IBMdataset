n = int(input())
a = list(map(int,input().split()))
mod = [0]*4
for i in a:
    mod[i%4] += 1
if mod[0]*2 + mod[2] >= n or mod[0]*2+1 >= n:
    print("Yes")
else:
    print("No")


