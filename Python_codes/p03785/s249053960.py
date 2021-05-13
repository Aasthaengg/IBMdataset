n,c,k=map(int, input().split())
t=[int(input()) for _ in range(n)]
t.sort()
tmp_lim=t[0]+k
num_bus=0
num_person=1
for i in range(1, n):
    if tmp_lim<t[i] or c<=num_person:
        num_bus+=1
        tmp_lim=t[i]+k
        num_person=1
    else:
        num_person+=1
    # print(num_bus, num_person, tmp_lim)
print(num_bus+1)