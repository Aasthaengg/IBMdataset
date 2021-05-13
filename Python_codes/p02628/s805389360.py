n,k = map(int, input().split())
lst_p=list()
tot=0

lst_p=input().split()
lst_p=list(map(int,lst_p))

def sort(my_list):
    size = len(my_list)
    for i in range(size):
        for j in range(size-i-1):
            if(my_list[j] > my_list[j+1]):
                tmp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = tmp
    return my_list

lst_p = sort(lst_p)

for i in range(k):
    tot += lst_p[i]
print(tot)
