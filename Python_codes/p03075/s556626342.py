a=[]
for i in range(5):
    a.append(int(input()))
a=sorted(a)
k=int(input())

if a[4]-a[0]>k:
    print(":(")
else:
    print("Yay!")