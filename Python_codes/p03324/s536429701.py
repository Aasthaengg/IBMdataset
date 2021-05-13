D,N = map(int,input().split())
count =0
number = 0
list=[]
while count < 100:
    number+= 1
    if number % 100 != 0:
        count += 1
        list.append(number)

print(list[N-1]*pow(100,D))