def insertion_sort(num_list,gap):
    global cnt 

    for i in range(gap,len(num_list)):
        evc = num_list[i]
        j   = i-gap
        while j >= 0 and num_list[j] > evc:
            num_list[j+gap] = num_list[j]
            j = j-gap
            cnt += 1
            num_list[j+gap] = evc

def shell_sort(num_list):
    global cnt
    cnt = 0
    m_list = []
    h = 1
    while h <= len(num_list):
        m_list.append(h)
        h = 3*h+1
    m_list.reverse()
    m = len(m_list)

    print(m)
    print(' '.join([str(i) for i in m_list]))
    for i in range(m):
        insertion_sort(num_list,m_list[i])

n = int(input())
num_list = [int(input()) for _ in range(n)]

shell_sort(num_list)
print(cnt)
for num in num_list:
    print(num)
