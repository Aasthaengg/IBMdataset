x = int(input())

lst = []
for i in range(1,101):
    for j in range(2,10):
       lst.append(i**j)
lst.sort(reverse=True)

for n in lst:
    if n <= x:
        print(n)
        break