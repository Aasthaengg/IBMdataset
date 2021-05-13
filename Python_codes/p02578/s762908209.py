
n = int(input())
l = list(map(int,input().split()))
height_stool = 0

temp = [i for i in l]
for i in range(n-1):
    if l[i] > l[i+1]:
        diff = l[i]-l[i+1]
        height_stool += diff
        l[i+1] += diff
print(height_stool)
