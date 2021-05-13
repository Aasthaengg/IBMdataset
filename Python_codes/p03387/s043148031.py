#和を求める解法
a,b,c = map(int,input().split(" "))
sum = a+b+c
max = max(a,b,c)
if (sum - max)%2 == 0:
    print(int((max*3 - sum)/2))
else:
    print(int(((max+1)*3 - sum)/2))