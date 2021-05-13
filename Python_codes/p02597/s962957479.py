N = int(input())
c = input()

r_count = 0
for i in range(N):
    if c[i]=="R":
        r_count+=1

r_remain = 0
for i in range(r_count,N):
    if c[i]=="R":
        r_remain+=1

print(r_remain)

