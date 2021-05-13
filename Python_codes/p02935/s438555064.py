N = int(input())
ls = list(map(int,input().split()))
ls.sort()
ave = ls[0]
for i in ls:
    ave = (ave + i)/2
print(ave)