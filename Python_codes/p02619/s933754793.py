days = int(input())
clast = list(map(int,input().split()))

allpref = [] #allpref[day][contest]
for i in range(days):
    allpref.append(list(map(int,input().split())))
donelist = [0]*26
resultlist = []
result = 0
for i in range(days):
    held = int(input())

    donelist[held-1] = i+1
    zanen = sum([clast[j]*((i+1)-donelist[j]) for j in range(26)])

    result += allpref[i][held-1] -zanen
    resultlist.append(result)

for num in resultlist:
    print(num)
