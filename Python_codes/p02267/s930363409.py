def linear_search(s,t):
    count = 0
    check_list = []
    for i in s:
        for j in t:
            if i == j and (j in check_list) == False:
                count = count + 1
                check_list.append(j)
    return count

sline = []
tline = []

n = int(input())

sline = list(map(int,input().split()))
if len(sline) != n:
    print("Error")
    exit()

q = int(input())

tline = list(map(int,input().split()))
if len(tline) != q:
    print("Error")
    print(len(tline),q)
    exit()

count = linear_search(sline,tline)

print(count)

