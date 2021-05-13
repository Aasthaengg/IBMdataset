h,w = map(int,input().split())
table = [["#"]*(w+2) for i in range(h+2)]
for i in range(1,h+1):
    a_list = list(input())
    for j in range(1,w+1):
        table[i][j] = a_list[j-1]
for i in range(h+2):
    print("".join(table[i]))