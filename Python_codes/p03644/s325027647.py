N=int(input())
list=[]
for i in range(7):
    s=2**i
    if s<=N:
        list.append(s)
    else:
        break
print(max(list))
