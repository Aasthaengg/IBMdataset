n=int(input())
kuku=set()
for i in range(1,10):
    for j in range(1,10):
        kuku.add(i*j)
if n in kuku:
    print("Yes")
else:
    print("No")