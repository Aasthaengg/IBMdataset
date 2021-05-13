A,B = input().split()

max_num = max(int(A),int(B))
min_num = min(int(A),int(B))
i = 0
flag = False

while flag == False:
    i += 1
    if (max_num*i)% min_num == 0:
        print(max_num*i)
        flag = True