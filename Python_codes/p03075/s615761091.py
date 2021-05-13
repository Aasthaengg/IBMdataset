def ip():return int(input())
a=[]
for i in range(5):
    a.append(ip())
k=ip()

for i in range(4):
    for j in range(i+1,5):
        if a[j]-a[i]>k:
            print(":(")
            exit()
print("Yay!")
