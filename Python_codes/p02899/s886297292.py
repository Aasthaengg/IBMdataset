num = int(input())
str_line = input().split(" ")
num_line = [int(n) for n in str_line]

rank_line = [0 for i in range(num)]

for i in range(num):
    rank_line[num_line[i] - 1] = i+1

for i in range(num):
    print(rank_line[i],end="")
    if(i != num-1):
        print(" ",end="")
