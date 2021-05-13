n = int(input())
li = []
for i in range(n):
    a,b = input().split()
    li.append([i+1,a,int(b)])
lia = sorted(li, key = lambda x:(x[1],-x[2]))
for i in range(n):
    print(lia[i][0])