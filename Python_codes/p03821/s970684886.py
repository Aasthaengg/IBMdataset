N = int(input())

a_list = []

b_list = []

for i in range(N):
    a,b = map(int,input().split())
    a_list.append(a)
    b_list.append(b)

a_list = a_list[::-1]
b_list = b_list[::-1]

#print(a_list)
#print(b_list)

st = 0

for i in range(N):
    a_list[i] += st
    if a_list[i] % b_list[i]:
        if a_list[i] < b_list[i]:
            st += b_list[i]-a_list[i]
        elif a_list[i] > b_list[i]:
            st += b_list[i]*((a_list[i]//b_list[i])+1)-a_list[i]
print(st)