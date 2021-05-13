def judge(int):
    if int == 2:return 1
    elif int <= 1 :return 0
    i = 2
    while i*i <= int:
        if int % i == 0:return 0 
        i += 1
    return 1



n = input()
count = 0
for i in range(n):
    if judge(input()) == 1:
        count+=1
print count