import random
i = input()
len_i = len(i)
num = 0
if len_i!=3:
    num = random.randint(0, len_i-4)
print(i[num]+i[num+1]+i[num+2])