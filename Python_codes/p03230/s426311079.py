n = int(input())
t = int((n*2)**(0.5))
if t*(t+1)//2!=n:
    print("No")
    quit()
l = [[] for _ in range(t+1)]
ind = 1
for i in range(t,0,-1):
    for j in range(i):
        l[t-i].append(j+ind)
    for j in range(i):
        l[t-i+1+j].append(j+ind)
    ind += i
print("Yes")
print(t+1)
for i in range(t+1):
    print(t,*l[i])