n = int(input())
a = list(map(int,input().split()))
a2 = list(map(lambda x:x*2,a))
All = sum(a)
p = All-sum(a2[1::2])
a3 = [p]
for i in range(n-1) :
    p = a[i]*2 - p
    a3.append(p)
mountain = ""
for j in range(n) :
    mountain += str(a3[j])
    if j == n-1 :
        print(mountain)
        exit()
    mountain += " "