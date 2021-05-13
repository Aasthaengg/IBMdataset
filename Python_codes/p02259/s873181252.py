n = input()
lst = map(int, raw_input().split())
flag = True
cnt=0
while flag:
    flag = False
    for j in range(n-1,0,-1):
        if lst[j] < lst[j-1]:
            tmp=lst[j-1]
            lst[j-1] = lst[j]
            lst[j] = tmp
            flag = True
            cnt+=1

print " ".join(map(str, (lst)))
print cnt