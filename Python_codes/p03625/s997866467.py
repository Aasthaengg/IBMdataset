n = int(input())
lst = list(map(int, input().split()))
lst.sort()
count = []

i = 0
while i<n-1:
    if lst[i]==lst[i+1]:
        count.append(lst[i])
        i+=2
    else:
        i+=1

count.sort(reverse=True)
count.append(0)
count.append(0)

print(count[0]*count[1])
