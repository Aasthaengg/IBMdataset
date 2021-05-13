li=[]

for i in range(5):
    li.append(int(input()))

k=int(input())

li.sort()


if li[-1]-li[0]>k:
    print(":(")
else:
    print("Yay!")
